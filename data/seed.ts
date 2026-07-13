import { NidaaEntry } from "../lib/types";

// Seed entries are illustrative / illustrative only — NOT real operational data.
// They exist so the board is not empty on first run and demonstrate the model.
// Coordinates are approximate city centers for map display.
export const SEED_ENTRIES: NidaaEntry[] = [
  {
    id: "seed-1",
    clientId: "seed-1",
    type: "offer",
    category: "medical",
    titleAr: "عيادة متنقلة في حلب — رعاية أولية مجانية",
    titleEn: "Mobile clinic in Aleppo — free primary care",
    bodyAr:
      "عيادة متنقلة تقدم رعاية أولية و لقاحات للأطفال أيام الثلاثاء والخميس. لا يشترط تسجيل مسبق.",
    bodyEn:
      "A mobile clinic providing primary care and child vaccinations on Tuesdays and Thursdays. No pre-registration required.",
    city: "Aleppo",
    contact: " through local committee",
    lat: 36.2021,
    lng: 37.1343,
    authorRole: "ngo",
    verified: true,
    region: "syr",
    createdAt: "2026-07-01T09:00:00.000Z",
    syncedAt: "2026-07-01T09:00:00.000Z",
  },
  {
    id: "seed-2",
    clientId: "seed-2",
    type: "need",
    category: "water",
    titleAr: "حاجة إلى خزانات مياه في مخيم إدلب",
    titleEn: "Need water tanks in Idlib camp",
    bodyAr:
      "نحتاج 20 خزان مياه نظيفة سعة 1000 لتر للعائلات النازحة في القطاع الشمالي.",
    bodyEn:
      "We need 20 clean 1000L water tanks for displaced families in the northern sector.",
    city: "Idlib",
    lat: 35.9303,
    lng: 36.6333,
    authorRole: "volunteer",
    verified: true,
    region: "syr",
    createdAt: "2026-07-03T12:30:00.000Z",
    syncedAt: "2026-07-03T12:30:00.000Z",
  },
  {
    id: "seed-3",
    clientId: "seed-3",
    type: "offer",
    category: "education",
    titleAr: "صفوف تعليمية مجانية للأطفال — دمشق",
    titleEn: "Free classes for children — Damascus",
    bodyAr:
      "متطوعون يقدمون دروس دعم في الرياضيات والعربية للصفوف 1–6، خمسة أيام في الأسبوع.",
    bodyEn:
      "Volunteers offer math and Arabic support classes for grades 1–6, five days a week.",
    city: "Damascus",
    lat: 33.5138,
    lng: 36.2765,
    authorRole: "volunteer",
    verified: false,
    region: "syr",
    createdAt: "2026-07-05T08:15:00.000Z",
    syncedAt: "2026-07-05T08:15:00.000Z",
  },
  {
    id: "seed-4",
    clientId: "seed-4",
    type: "need",
    category: "food",
    titleAr: "طلب مساعدة غذائية — ريف حمص",
    titleEn: "Request food assistance — Rural Homs",
    bodyAr:
      "عائلة نازحة مكونة من 7 أفراد بحاجة إلى سلة غذائية شهرية. متاح تواصل عبر لجنة الحي.",
    bodyEn:
      "Displaced family of 7 needs a monthly food basket. Contact available via neighborhood committee.",
    city: "Homs",
    lat: 34.7103,
    lng: 36.2873,
    authorRole: "individual",
    verified: false,
    region: "syr",
    createdAt: "2026-07-07T17:45:00.000Z",
    syncedAt: "2026-07-07T17:45:00.000Z",
  },
  {
    id: "seed-5",
    clientId: "seed-5",
    type: "offer",
    category: "shelter",
    titleAr: "مأوى مؤقت متاح في درعا",
    titleEn: "Temporary shelter available in Daraa",
    bodyAr:
      "مبنى يوفر 15 مكان إقامة مؤقت مع فرش وبطانيات للعائلات النازحة. التنسيق عبر لجنة المحافظة.",
    bodyEn:
      "A building offers 15 temporary spaces with mattresses and blankets for displaced families. Coordination via governorate committee.",
    city: "Daraa",
    lat: 32.5193,
    lng: 36.2323,
    authorRole: "ngo",
    verified: true,
    region: "syr",
    createdAt: "2026-07-08T10:00:00.000Z",
    syncedAt: "2026-07-08T10:00:00.000Z",
  },
];
