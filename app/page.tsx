"use client";

import { useCallback, useEffect, useMemo, useState } from "react";
import {
  allLocal,
  pendingLocal,
  saveLocal,
  markSynced,
  removeLocal,
  QueuedEntry,
} from "@/lib/offlineQueue";
import { NidaaEntry, Lang } from "@/lib/types";
import dynamic from "next/dynamic";

// Map is client-only (Leaflet needs window); load lazily.
const BoardMap = dynamic(() => import("@/components/BoardMap"), { ssr: false });

type Filter = "all" | "need" | "offer";
type View = "list" | "map";
type Region = "all" | "gza" | "wb" | "syr";

interface ServerEntry extends NidaaEntry {}

export default function Page() {
  const [lang, setLang] = useState<Lang>("ar");
  const [online, setOnline] = useState<boolean>(true);
  const [local, setLocal] = useState<QueuedEntry[]>([]);
  const [server, setServer] = useState<ServerEntry[]>([]);
  const [filter, setFilter] = useState<Filter>("all");
  const [region, setRegion] = useState<Region>("all");
  const [city, setCity] = useState<string>("");
  const [view, setView] = useState<View>("list");
  const [syncing, setSyncing] = useState<boolean>(false);
  const [showForm, setShowForm] = useState<boolean>(false);
  const [lastSync, setLastSync] = useState<string>("");

  const t = (ar: string, en: string) => (lang === "ar" ? ar : en);

  // ---- connectivity tracking ----
  useEffect(() => {
    const update = () => setOnline(navigator.onLine);
    update();
    window.addEventListener("online", update);
    window.addEventListener("offline", update);
    return () => {
      window.removeEventListener("online", update);
      window.removeEventListener("offline", update);
    };
  }, []);

  // ---- register service worker (once) ----
  useEffect(() => {
    if ("serviceWorker" in navigator) {
      navigator.serviceWorker.register("/sw.js").catch(() => {});
    }
  }, []);

  const refreshLocal = useCallback(async () => {
    setLocal(await allLocal());
  }, []);

  // ---- pull from server ----
  const pull = useCallback(async () => {
    if (!navigator.onLine) return;
    try {
      const res = await fetch("/api/entries", { cache: "no-store" });
      if (!res.ok) return;
      const data = (await res.json()) as { entries: ServerEntry[] };
      setServer(data.entries || []);
      setLastSync(new Date().toLocaleTimeString());
    } catch {
      /* offline — ignore */
    }
  }, []);

  // ---- push pending to server ----
  const pushPending = useCallback(async () => {
    const pending = await pendingLocal();
    if (pending.length === 0) return;
    setSyncing(true);
    for (const entry of pending) {
      try {
        const res = await fetch("/api/entries", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(entry),
        });
        if (res.ok) {
          const data = (await res.json()) as { entry: NidaaEntry };
          await markSynced(entry.clientId, data.entry.syncedAt || new Date().toISOString());
        }
      } catch {
        // stays pending; will retry next time
      }
    }
    setSyncing(false);
    await refreshLocal();
    await pull();
  }, [pull, refreshLocal]);

  // initial load
  useEffect(() => {
    refreshLocal().then(pull);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  // auto-sync when coming online
  useEffect(() => {
    if (online) {
      pushPending().then(pull);
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [online]);

  // ---- merged view: local (incl. pending) + server, deduped by clientId ----
  const merged = useMemo(() => {
    const map = new Map<string, QueuedEntry>();
    for (const s of server) {
      map.set(s.clientId, { ...s, syncedAt: s.syncedAt });
    }
    for (const l of local) {
      map.set(l.clientId, l); // local wins (may be newer / pending)
    }
    let arr = Array.from(map.values());
    if (filter !== "all") arr = arr.filter((e) => e.type === filter);
    if (region !== "all") arr = arr.filter((e) => (e.region ? e.region === region : true));
    if (city.trim()) arr = arr.filter((e) => e.city.toLowerCase().includes(city.trim().toLowerCase()));
    return arr.sort(
      (a, b) => new Date(b.createdAt).getTime() - new Date(a.createdAt).getTime()
    );
  }, [local, server, filter, region, city]);

  const pendingCount = useMemo(() => local.filter((e) => !e.syncedAt).length, [local]);

  // ---- submit new entry (offline-first: save local first) ----
  async function submit(newEntry: Omit<QueuedEntry, "clientId" | "id" | "createdAt" | "syncedAt" | "verified">) {
    const clientId =
      (crypto.randomUUID && crypto.randomUUID()) ||
      "c-" + Math.random().toString(36).slice(2) + Date.now().toString(36);
    const entry: QueuedEntry = {
      ...newEntry,
      clientId,
      id: clientId,
      verified: false, // local posts start unverified
      createdAt: new Date().toISOString(),
      syncedAt: null, // pending
    } as QueuedEntry;
    await saveLocal(entry);
    await refreshLocal();
    if (navigator.onLine) {
      await pushPending();
    }
    setShowForm(false);
  }

  return (
    <div className="app">
      <header className="top">
        <h1>نداء · Nidaa</h1>
        <p>
          {t(
            "لوحة احتياجات وخدمات المجتمع في سوريا — تعمل بدون إنترنت.",
            "Community needs & services board for Syria — works without internet."
          )}
        </p>
      </header>

      <div className="statusbar">
        <span className={"pill " + (online ? "online" : "offline")}>
          {online ? t("متصل", "Online") : t("غير متصل — يعمل محلياً", "Offline — working locally")}
        </span>
        {pendingCount > 0 && (
          <span className="pill pending">
            {t(`${pendingCount} منشور بانتظار المزامنة`, `${pendingCount} post(s) pending sync`)}
          </span>
        )}
        <span style={{ marginInlineStart: "auto" }}>
          <button className="btn secondary" onClick={() => setLang(lang === "ar" ? "en" : "ar")}>
            {lang === "ar" ? "EN" : "ع"}
          </button>
        </span>
        <button className="btn" onClick={() => pushPending()} disabled={syncing || !online}>
          {syncing ? t("جارٍ المزامنة…", "Syncing…") : t("مزامنة الآن", "Sync now")}
        </button>
      </div>

      <div className="notice">
        {t(
          "يعمل التطبيق حتى بدون إنترنت: أي منشور جديد يُحفظ على جهازك ويرسل تلقائياً عند توفر الاتصال. بيانات المرافق مصدرها HDX / HOT OSM (موثّقة). الخريطة تخزّن البلاطات محلياً للعمل دون اتصال.",
          "Works offline: new posts save on your device and sync when a connection appears. Facility data is from HDX / HOT OSM (verified). Map tiles are cached locally for offline use."
        )}
      </div>

      <div className="controls">
        <select value={filter} onChange={(e) => setFilter(e.target.value as Filter)}>
          <option value="all">{t("الكل", "All")}</option>
          <option value="need">{t("احتياجات", "Needs")}</option>
          <option value="offer">{t("عروض", "Offers")}</option>
        </select>
        <select value={region} onChange={(e) => setRegion(e.target.value as Region)}>
          <option value="all">{t("كل المناطق", "All regions")}</option>
          <option value="gza">{t("غزة", "Gaza Strip")}</option>
          <option value="wb">{t("الضفة الغربية", "West Bank")}</option>
          <option value="syr">{t("سوريا", "Syria")}</option>
        </select>
        <select value={view} onChange={(e) => setView(e.target.value as View)}>
          <option value="list">{t("قائمة", "List")}</option>
          <option value="map">{t("خريطة", "Map")}</option>
        </select>
        <input
          type="search"
          placeholder={t("بحث بالمدينة…", "Search by city…")}
          value={city}
          onChange={(e) => setCity(e.target.value)}
        />
        <button className="btn" style={{ marginInlineStart: "auto" }} onClick={() => setShowForm((s) => !s)}>
          {t("+ منشور جديد", "+ New post")}
        </button>
      </div>

      {showForm && <NewPostForm lang={lang} t={t} onSubmit={submit} onCancel={() => setShowForm(false)} />}

      {view === "map" ? (
        <BoardMap entries={merged} lang={lang} />
      ) : (
        <>
          {merged.length === 0 && (
            <div className="skeleton">{t("لا توجد منشورات بعد.", "No posts yet.")}</div>
          )}

          {merged.map((e) => (
            <div className="card" key={e.clientId}>
              <div className="row1">
                <div>
                  <span className={"tag " + e.type}>{t(e.type === "need" ? "احتياج" : "عرض", e.type === "need" ? "NEED" : "OFFER")}</span>{" "}
                  <span className="tag cat">{e.category}</span>{" "}
                  <span className={"tag " + (e.verified ? "verified" : "unverified")}>
                    {e.verified ? t("موثّق", "Verified") : t("غير موثّق", "Unverified")}
                  </span>
                </div>
                {!e.syncedAt && <span className="tag unverified">{t("بانتظار المزامنة", "Pending")}</span>}
              </div>
              <h3>{lang === "ar" ? e.titleAr : e.titleEn}</h3>
              <div>{lang === "ar" ? e.bodyAr : e.bodyEn}</div>
              <div className="meta">
                📍 {e.city} · {t("النوع", "Role")}: {e.authorRole}
                {e.contact ? " · ☎ " + e.contact : ""}
                {e.lat && e.lng ? " · 🗺 " + e.lat.toFixed(2) + "," + e.lng.toFixed(2) : ""}
              </div>
            </div>
          ))}
        </>
      )}

      <footer className="foot">
        {t(
          "نداء نموذج أولي — البيانات توضيحية وليست معلومات تشغيلية حية. يجب تأمين التحقق بصلاحيات في الإصدار الإنتاجي.",
          "Nidaa is a prototype — data is illustrative, not live operational info. Verification must be auth-gated in production."
        )}
      </footer>
    </div>
  );
}

function NewPostForm({
  lang,
  t,
  onSubmit,
  onCancel,
}: {
  lang: Lang;
  t: (ar: string, en: string) => string;
  onSubmit: (e: any) => void;
  onCancel: () => void;
}) {
  const [type, setType] = useState<"need" | "offer">("need");
  const [category, setCategory] = useState<NidaaEntry["category"]>("food");
  const [titleAr, setTitleAr] = useState("");
  const [titleEn, setTitleEn] = useState("");
  const [bodyAr, setBodyAr] = useState("");
  const [bodyEn, setBodyEn] = useState("");
  const [city, setCity] = useState("");
  const [contact, setContact] = useState("");
  const [role, setRole] = useState<NidaaEntry["authorRole"]>("volunteer");
  const [lat, setLat] = useState("");
  const [lng, setLng] = useState("");

  const canSubmit = titleAr.trim().length > 0 && city.trim().length > 0;

  return (
    <div className="card">
      <div className="form-grid">
        <div className="two">
          <div>
            <label>{t("النوع", "Type")}</label>
            <select value={type} onChange={(e) => setType(e.target.value as any)}>
              <option value="need">{t("احتياج", "Need")}</option>
              <option value="offer">{t("عرض", "Offer")}</option>
            </select>
          </div>
          <div>
            <label>{t("التصنيف", "Category")}</label>
            <select value={category} onChange={(e) => setCategory(e.target.value as any)}>
              <option value="medical">{t("طبي", "Medical")}</option>
              <option value="food">{t("غذاء", "Food")}</option>
              <option value="water">{t("مياه", "Water")}</option>
              <option value="shelter">{t("مأوى", "Shelter")}</option>
              <option value="education">{t("تعليم", "Education")}</option>
              <option value="transport">{t("نقل", "Transport")}</option>
              <option value="other">{t("أخرى", "Other")}</option>
            </select>
          </div>
        </div>

        <div>
          <label>{t("العنوان (عربي) *", "Title (Arabic) *")}</label>
          <input value={titleAr} onChange={(e) => setTitleAr(e.target.value)} placeholder={t("مثال: حاجة إلى مياه شرب", "e.g. Need drinking water")} />
        </div>
        <div>
          <label>{t("العنوان (إنجليزي)", "Title (English)")}</label>
          <input value={titleEn} onChange={(e) => setTitleEn(e.target.value)} />
        </div>
        <div>
          <label>{t("التفاصيل (عربي)", "Details (Arabic)")}</label>
          <textarea value={bodyAr} onChange={(e) => setBodyAr(e.target.value)} />
        </div>
        <div>
          <label>{t("التفاصيل (إنجليزي)", "Details (English)")}</label>
          <textarea value={bodyEn} onChange={(e) => setBodyEn(e.target.value)} />
        </div>
        <div className="two">
          <div>
            <label>{t("المدينة *", "City *")}</label>
            <input value={city} onChange={(e) => setCity(e.target.value)} placeholder="Aleppo" />
          </div>
          <div>
            <label>{t("جهة النشر", "Your role")}</label>
            <select value={role} onChange={(e) => setRole(e.target.value as any)}>
              <option value="individual">{t("فرد", "Individual")}</option>
              <option value="volunteer">{t("متطوع", "Volunteer")}</option>
              <option value="ngo">{t("منظمة", "NGO")}</option>
              <option value="unknown">{t("غير محدد", "Unknown")}</option>
            </select>
          </div>
        </div>
        <div>
          <label>{t("وسيلة التواصل (اختياري)", "Contact (optional)")}</label>
          <input value={contact} onChange={(e) => setContact(e.target.value)} />
        </div>
        <div className="two">
          <div>
            <label>{t("خط العرض (اختياري)", "Latitude (optional)")}</label>
            <input value={lat} onChange={(e) => setLat(e.target.value)} placeholder="36.20" />
          </div>
          <div>
            <label>{t("خط الطول (اختياري)", "Longitude (optional)")}</label>
            <input value={lng} onChange={(e) => setLng(e.target.value)} placeholder="37.13" />
          </div>
        </div>

        <div className="two" style={{ marginTop: 8 }}>
          <button className="btn" disabled={!canSubmit} onClick={() =>
            onSubmit({
              type,
              category,
              titleAr,
              titleEn,
              bodyAr,
              bodyEn,
              city,
              contact: contact || undefined,
              authorRole: role,
              lat: lat ? Number(lat) : undefined,
              lng: lng ? Number(lng) : undefined,
            })
          }>
            {t("حفظ ونشر", "Save & post")}
          </button>
          <button className="btn secondary" onClick={onCancel}>{t("إلغاء", "Cancel")}</button>
        </div>
      </div>
    </div>
  );
}
