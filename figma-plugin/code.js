figma.showUI(__html__, { width: 360, height: 420 });

// Helper: RGB 0-255 to 0-1
function rgb(r, g, b) {
  return { r: r / 255, g: g / 255, b: b / 255 };
}

function solidPaint(r, g, b, a = 1) {
  return [{ type: 'SOLID', color: rgb(r, g, b), opacity: a }];
}

async function loadFonts() {
  await figma.loadFontAsync({ family: "Inter", style: "Regular" });
  await figma.loadFontAsync({ family: "Inter", style: "Medium" });
  await figma.loadFontAsync({ family: "Inter", style: "Semi Bold" });
  await figma.loadFontAsync({ family: "Inter", style: "Bold" });
}

function createText(text, size = 14, style = "Regular", color = rgb(15, 23, 42)) {
  const t = figma.createText();
  t.fontName = { family: "Inter", style: style };
  t.characters = text;
  t.fontSize = size;
  t.fills = [{ type: 'SOLID', color: color }];
  return t;
}

function createScreen(name, x, y, bg = rgb(255, 255, 255)) {
  const frame = figma.createFrame();
  frame.name = name;
  frame.resize(393, 852);
  frame.x = x;
  frame.y = y;
  frame.fills = [{ type: 'SOLID', color: bg }];
  frame.cornerRadius = 40;
  frame.clipsContent = true;
  
  // Status Bar
  const statusBar = figma.createFrame();
  statusBar.name = "Status Bar";
  statusBar.resize(393, 44);
  statusBar.fills = [];
  const time = createText("9:41", 14, "Semi Bold", rgb(100, 116, 139));
  time.x = 24;
  time.y = 14;
  statusBar.appendChild(time);
  const icons = createText("5G  100%", 12, "Medium", rgb(100, 116, 139));
  icons.x = 310;
  icons.y = 15;
  statusBar.appendChild(icons);
  frame.appendChild(statusBar);

  return frame;
}

function createButton(text, bg = rgb(249, 115, 22), textCol = rgb(255, 255, 255), width = 345, height = 52) {
  const btn = figma.createFrame();
  btn.name = "Button - " + text;
  btn.resize(width, height);
  btn.cornerRadius = 14;
  btn.fills = [{ type: 'SOLID', color: bg }];
  btn.layoutMode = "HORIZONTAL";
  btn.primaryAxisAlignItems = "CENTER";
  btn.counterAxisAlignItems = "CENTER";
  
  const label = createText(text, 15, "Bold", textCol);
  btn.appendChild(label);
  return btn;
}

// -----------------------------------------------------------------------------
// EXP 12: CAMPUSBITE WIREFRAMES
// -----------------------------------------------------------------------------
async function buildExp12CampusBite() {
  await loadFonts();
  const startX = 0;
  const screens = [];

  // Screen 1: Splash
  const s1 = createScreen("01_Wireframe_Splash", startX, 0, rgb(248, 250, 252));
  const logoBox = figma.createFrame();
  logoBox.resize(90, 90);
  logoBox.cornerRadius = 24;
  logoBox.fills = solidPaint(203, 213, 225);
  logoBox.x = (393 - 90) / 2;
  logoBox.y = 260;
  s1.appendChild(logoBox);

  const t1 = createText("CampusBite", 26, "Bold", rgb(30, 41, 59));
  t1.x = (393 - t1.width) / 2;
  t1.y = 370;
  s1.appendChild(t1);

  const sub1 = createText("NIE Mysuru Smart Canteen Ordering", 13, "Regular", rgb(100, 116, 139));
  sub1.x = (393 - sub1.width) / 2;
  sub1.y = 410;
  s1.appendChild(sub1);

  const btn1 = createButton("Get Started →", rgb(71, 85, 105), rgb(255, 255, 255));
  btn1.x = 24;
  btn1.y = 730;
  s1.appendChild(btn1);
  screens.push(s1);

  // Screen 2: Auth
  const s2 = createScreen("02_Wireframe_Login", startX + 460, 0, rgb(255, 255, 255));
  const h2 = createText("Student Login", 24, "Bold", rgb(15, 23, 42));
  h2.x = 24;
  h2.y = 100;
  s2.appendChild(h2);

  const sub2 = createText("Enter your college USN to continue", 13, "Regular", rgb(100, 116, 139));
  sub2.x = 24;
  sub2.y = 135;
  s2.appendChild(sub2);

  const input1 = figma.createFrame();
  input1.name = "Input_USN";
  input1.resize(345, 50);
  input1.cornerRadius = 10;
  input1.fills = solidPaint(241, 245, 249);
  input1.strokes = solidPaint(203, 213, 225);
  input1.x = 24;
  input1.y = 200;
  const inText1 = createText("USN: 4NI25CS130", 14, "Medium", rgb(71, 85, 105));
  inText1.x = 16;
  inText1.y = 16;
  input1.appendChild(inText1);
  s2.appendChild(input1);

  const input2 = figma.createFrame();
  input2.name = "Input_Password";
  input2.resize(345, 50);
  input2.cornerRadius = 10;
  input2.fills = solidPaint(241, 245, 249);
  input2.strokes = solidPaint(203, 213, 225);
  input2.x = 24;
  input2.y = 270;
  const inText2 = createText("••••••••••••", 14, "Medium", rgb(148, 163, 184));
  inText2.x = 16;
  inText2.y = 16;
  input2.appendChild(inText2);
  s2.appendChild(input2);

  const btn2 = createButton("Sign In to Canteen", rgb(71, 85, 105));
  btn2.x = 24;
  btn2.y = 360;
  s2.appendChild(btn2);
  screens.push(s2);

  // Screen 3: Home Dashboard
  const s3 = createScreen("03_Wireframe_Dashboard", startX + 920, 0, rgb(248, 250, 252));
  const h3 = createText("Hey, Nithyashree! 👋", 20, "Bold", rgb(15, 23, 42));
  h3.x = 24;
  h3.y = 70;
  s3.appendChild(h3);

  const banner = figma.createFrame();
  banner.resize(345, 130);
  banner.cornerRadius = 16;
  banner.fills = solidPaint(226, 232, 240);
  banner.x = 24;
  banner.y = 120;
  const bTitle = createText("Main Campus Food Court", 16, "Bold", rgb(30, 41, 59));
  bTitle.x = 20;
  bTitle.y = 30;
  banner.appendChild(bTitle);
  const bSub = createText("Current Crowd: Low • Prep Time: 10 mins", 12, "Regular", rgb(71, 85, 105));
  bSub.x = 20;
  bSub.y = 60;
  banner.appendChild(bSub);
  s3.appendChild(banner);

  const hCat = createText("Menu Categories", 16, "Bold", rgb(15, 23, 42));
  hCat.x = 24;
  hCat.y = 280;
  s3.appendChild(hCat);

  const categories = ["Breakfast", "Meals", "Beverages", "Snacks"];
  for (let i = 0; i < categories.length; i++) {
    const card = figma.createFrame();
    card.resize(162, 100);
    card.cornerRadius = 12;
    card.fills = solidPaint(255, 255, 255);
    card.strokes = solidPaint(226, 232, 240);
    card.x = 24 + (i % 2) * 183;
    card.y = 315 + Math.floor(i / 2) * 120;
    const catLabel = createText(categories[i], 14, "Bold", rgb(30, 41, 59));
    catLabel.x = 16;
    catLabel.y = 50;
    card.appendChild(catLabel);
    s3.appendChild(card);
  }
  screens.push(s3);

  // Screen 4: Food Details
  const s4 = createScreen("04_Wireframe_MenuDetail", startX + 1380, 0, rgb(255, 255, 255));
  const fImg = figma.createFrame();
  fImg.resize(393, 260);
  fImg.fills = solidPaint(226, 232, 240);
  s4.appendChild(fImg);

  const fTitle = createText("Masala Dosa with Sambar", 20, "Bold", rgb(15, 23, 42));
  fTitle.x = 24;
  fTitle.y = 290;
  s4.appendChild(fTitle);

  const fPrice = createText("₹50.00", 18, "Bold", rgb(71, 85, 105));
  fPrice.x = 24;
  fPrice.y = 325;
  s4.appendChild(fPrice);

  const fDesc = createText("Crispy golden fermented crepe served with spicy potato filling and fresh coconut chutney.", 13, "Regular", rgb(100, 116, 139));
  fDesc.x = 24;
  fDesc.y = 365;
  fDesc.resize(345, 60);
  s4.appendChild(fDesc);

  const btn4 = createButton("Add to Tray (1 Item) • ₹50", rgb(71, 85, 105));
  btn4.x = 24;
  btn4.y = 740;
  s4.appendChild(btn4);
  screens.push(s4);

  // Screen 5: Cart
  const s5 = createScreen("05_Wireframe_Cart", startX + 1840, 0, rgb(248, 250, 252));
  const h5 = createText("Order Summary", 22, "Bold", rgb(15, 23, 42));
  h5.x = 24;
  h5.y = 80;
  s5.appendChild(h5);

  const cartCard = figma.createFrame();
  cartCard.resize(345, 160);
  cartCard.cornerRadius = 16;
  cartCard.fills = solidPaint(255, 255, 255);
  cartCard.strokes = solidPaint(226, 232, 240);
  cartCard.x = 24;
  cartCard.y = 130;
  const item1 = createText("1x Masala Dosa .................... ₹50", 13, "Medium", rgb(51, 65, 85));
  item1.x = 20;
  item1.y = 25;
  cartCard.appendChild(item1);
  const item2 = createText("1x Cold Badam Milk ............ ₹30", 13, "Medium", rgb(51, 65, 85));
  item2.x = 20;
  item2.y = 60;
  cartCard.appendChild(item2);
  const total = createText("Total Payable: ₹80.00", 15, "Bold", rgb(15, 23, 42));
  total.x = 20;
  total.y = 110;
  cartCard.appendChild(total);
  s5.appendChild(cartCard);

  const btn5 = createButton("Confirm & Pay (₹80)", rgb(71, 85, 105));
  btn5.x = 24;
  btn5.y = 740;
  s5.appendChild(btn5);
  screens.push(s5);

  // Screen 6: Live Order Status
  const s6 = createScreen("06_Wireframe_OrderStatus", startX + 2300, 0, rgb(255, 255, 255));
  const tokenBox = figma.createFrame();
  tokenBox.resize(200, 140);
  tokenBox.cornerRadius = 20;
  tokenBox.fills = solidPaint(241, 245, 249);
  tokenBox.strokes = solidPaint(203, 213, 225);
  tokenBox.x = (393 - 200) / 2;
  tokenBox.y = 160;
  const tokenLbl = createText("TOKEN NO", 12, "Bold", rgb(100, 116, 139));
  tokenLbl.x = (200 - tokenLbl.width) / 2;
  tokenLbl.y = 25;
  tokenBox.appendChild(tokenLbl);
  const tokenNum = createText("#B-104", 32, "Bold", rgb(30, 41, 59));
  tokenNum.x = (200 - tokenNum.width) / 2;
  tokenNum.y = 55;
  tokenBox.appendChild(tokenNum);
  s6.appendChild(tokenBox);

  const stMsg = createText("Food is being prepared! 🍳", 18, "Bold", rgb(15, 23, 42));
  stMsg.x = (393 - stMsg.width) / 2;
  stMsg.y = 340;
  s6.appendChild(stMsg);

  const stEst = createText("Estimated collection time: 10 mins\nPickup Counter 2 (NIE Canteen)", 13, "Regular", rgb(100, 116, 139));
  stEst.x = (393 - stEst.width) / 2;
  stEst.y = 380;
  s6.appendChild(stEst);
  screens.push(s6);

  figma.viewport.scrollAndZoomIntoView(screens);
  return { count: 6, screens: screens.map(s => s.name) };
}

// -----------------------------------------------------------------------------
// EXP 12: BOOKNEST WIREFRAMES
// -----------------------------------------------------------------------------
async function buildExp12BookNest() {
  await loadFonts();
  const startX = 0;
  const screens = [];

  // Screen 1: Catalog
  const s1 = createScreen("01_Wireframe_BookCatalog", startX, 0, rgb(248, 250, 252));
  const h1 = createText("BookNest 📚", 22, "Bold", rgb(15, 23, 42));
  h1.x = 24;
  h1.y = 70;
  s1.appendChild(h1);
  const sub1 = createText("NIE Mysuru Academic Textbook Portal", 13, "Regular", rgb(100, 116, 139));
  sub1.x = 24;
  sub1.y = 100;
  s1.appendChild(sub1);

  // Search input
  const search = figma.createFrame();
  search.resize(345, 46);
  search.cornerRadius = 10;
  search.fills = solidPaint(255, 255, 255);
  search.strokes = solidPaint(203, 213, 225);
  search.x = 24;
  search.y = 135;
  const sText = createText("🔍 Search by Subject, Author, or ISBN...", 13, "Regular", rgb(148, 163, 184));
  sText.x = 16;
  sText.y = 14;
  search.appendChild(sText);
  s1.appendChild(search);

  // Book Cards
  const books = [
    { title: "DevOps Engineering Practices", auth: "Dr. K. Sharma", sem: "4th Sem CSE", price: "₹250 (Used)" },
    { title: "Database System Concepts", auth: "Silberschatz", sem: "4th Sem CSE", price: "₹450 (New)" },
    { title: "Operating Systems Principles", auth: "Galvin & Gagne", sem: "4th Sem CSE", price: "₹300 (Used)" }
  ];

  for (let i = 0; i < books.length; i++) {
    const card = figma.createFrame();
    card.resize(345, 110);
    card.cornerRadius = 14;
    card.fills = solidPaint(255, 255, 255);
    card.strokes = solidPaint(226, 232, 240);
    card.x = 24;
    card.y = 210 + i * 130;
    
    const bImg = figma.createFrame();
    bImg.resize(60, 80);
    bImg.cornerRadius = 6;
    bImg.fills = solidPaint(203, 213, 225);
    bImg.x = 15;
    bImg.y = 15;
    card.appendChild(bImg);

    const bT = createText(books[i].title, 14, "Bold", rgb(30, 41, 59));
    bT.x = 90;
    bT.y = 18;
    card.appendChild(bT);

    const bA = createText(books[i].auth + " • " + books[i].sem, 12, "Regular", rgb(100, 116, 139));
    bA.x = 90;
    bA.y = 44;
    card.appendChild(bA);

    const bP = createText(books[i].price, 13, "Bold", rgb(15, 23, 42));
    bP.x = 90;
    bP.y = 70;
    card.appendChild(bP);

    s1.appendChild(card);
  }
  screens.push(s1);

  // Screen 2: Book Detail
  const s2 = createScreen("02_Wireframe_BookDetail", startX + 460, 0, rgb(255, 255, 255));
  const cov = figma.createFrame();
  cov.resize(160, 220);
  cov.cornerRadius = 10;
  cov.fills = solidPaint(203, 213, 225);
  cov.x = (393 - 160) / 2;
  cov.y = 90;
  s2.appendChild(cov);

  const dtTitle = createText("DevOps Engineering Practices", 18, "Bold", rgb(15, 23, 42));
  dtTitle.x = (393 - dtTitle.width) / 2;
  dtTitle.y = 330;
  s2.appendChild(dtTitle);

  const dtPrice = createText("₹250 • Good Condition (2nd Hand)", 14, "Semi Bold", rgb(71, 85, 105));
  dtPrice.x = (393 - dtPrice.width) / 2;
  dtPrice.y = 365;
  s2.appendChild(dtPrice);

  const dtDesc = createText("Official syllabus textbook covering Docker, Kubernetes, CI/CD pipelines, and microservices architecture at NIE Mysuru. Clean pages with minimal annotations.", 13, "Regular", rgb(100, 116, 139));
  dtDesc.x = 24;
  dtDesc.y = 415;
  dtDesc.resize(345, 80);
  s2.appendChild(dtDesc);

  const btnReserve = createButton("Reserve for Campus Pickup", rgb(71, 85, 105));
  btnReserve.x = 24;
  btnReserve.y = 740;
  s2.appendChild(btnReserve);
  screens.push(s2);

  // Screen 3: Peer Exchange
  const s3 = createScreen("03_Wireframe_PeerExchange", startX + 920, 0, rgb(248, 250, 252));
  const h3 = createText("Student Book Swap Hub", 20, "Bold", rgb(15, 23, 42));
  h3.x = 24;
  h3.y = 80;
  s3.appendChild(h3);

  const swapCard = figma.createFrame();
  swapCard.resize(345, 160);
  swapCard.cornerRadius = 16;
  swapCard.fills = solidPaint(255, 255, 255);
  swapCard.strokes = solidPaint(226, 232, 240);
  swapCard.x = 24;
  swapCard.y = 130;
  const swTitle = createText("Exchange Your Old Books", 15, "Bold", rgb(30, 41, 59));
  swTitle.x = 20;
  swTitle.y = 20;
  swapCard.appendChild(swTitle);
  const swSub = createText("Swap previous semester books directly with batchmates or junior students at NIE.", 13, "Regular", rgb(100, 116, 139));
  swSub.x = 20;
  swSub.y = 50;
  swSub.resize(305, 50);
  swapCard.appendChild(swSub);
  s3.appendChild(swapCard);
  screens.push(s3);

  figma.viewport.scrollAndZoomIntoView(screens);
  return { count: 3, screens: screens.map(s => s.name) };
}

// -----------------------------------------------------------------------------
// EXP 13: CAMPUSBITE HIGH-FIDELITY DESIGN & PROTOTYPE
// -----------------------------------------------------------------------------
async function buildExp13HighFidelity() {
  await loadFonts();
  const startX = 0;
  const screens = [];

  const COLOR_PRIMARY = rgb(249, 115, 22); // Vibrant Orange
  const COLOR_ACCENT = rgb(16, 185, 129);  // Fresh Green
  const COLOR_DARK = rgb(15, 23, 42);      // Slate 900
  const COLOR_BG = rgb(248, 250, 252);     // Slate 50
  const COLOR_CARD = rgb(255, 255, 255);

  // Screen 1: Splash Screen
  const s1 = createScreen("01_HiFi_Splash", startX, 0, COLOR_DARK);
  const logo = figma.createFrame();
  logo.resize(110, 110);
  logo.cornerRadius = 32;
  logo.fills = solidPaint(249, 115, 22);
  logo.x = (393 - 110) / 2;
  logo.y = 260;
  const iconText = createText("🍔", 48, "Bold", rgb(255, 255, 255));
  iconText.x = (110 - iconText.width) / 2;
  iconText.y = 24;
  logo.appendChild(iconText);
  s1.appendChild(logo);

  const t1 = createText("CampusBite", 32, "Bold", rgb(255, 255, 255));
  t1.x = (393 - t1.width) / 2;
  t1.y = 390;
  s1.appendChild(t1);

  const sub1 = createText("Smart Canteen Ordering for NIE Mysuru", 14, "Medium", rgb(148, 163, 184));
  sub1.x = (393 - sub1.width) / 2;
  sub1.y = 435;
  s1.appendChild(sub1);

  const btnGetStarted = createButton("Explore Menu →", COLOR_PRIMARY, rgb(255, 255, 255));
  btnGetStarted.x = 24;
  btnGetStarted.y = 730;
  s1.appendChild(btnGetStarted);
  screens.push(s1);

  // Screen 2: Food Discovery & Menu
  const s2 = createScreen("02_HiFi_DiscoverMenu", startX + 460, 0, COLOR_BG);
  
  // Header Greeting
  const hGreeting = createText("Hello, Nithyashree! 👋", 20, "Bold", COLOR_DARK);
  hGreeting.x = 24;
  hGreeting.y = 65;
  s2.appendChild(hGreeting);

  const hSub = createText("NIE Main Canteen • Open until 7:30 PM", 12, "Medium", rgb(100, 116, 139));
  hSub.x = 24;
  hSub.y = 95;
  s2.appendChild(hSub);

  // Promo Banner
  const banner = figma.createFrame();
  banner.resize(345, 120);
  banner.cornerRadius = 20;
  banner.fills = [{ type: 'SOLID', color: rgb(254, 243, 199) }];
  banner.x = 24;
  banner.y = 130;
  const bTag = createText("TODAY'S SPECIAL", 11, "Bold", rgb(217, 119, 6));
  bTag.x = 20;
  bTag.y = 20;
  banner.appendChild(bTag);
  const bHead = createText("Crispy Paneer Roll + Chai", 16, "Bold", COLOR_DARK);
  bHead.x = 20;
  bHead.y = 42;
  banner.appendChild(bHead);
  const bPrice = createText("Combo at ₹65 (Save 20%)", 13, "Semi Bold", rgb(180, 83, 9));
  bPrice.x = 20;
  bPrice.y = 72;
  banner.appendChild(bPrice);
  s2.appendChild(banner);

  // Food Cards Section
  const secTitle = createText("Popular Items 🔥", 18, "Bold", COLOR_DARK);
  secTitle.x = 24;
  secTitle.y = 275;
  s2.appendChild(secTitle);

  const foodItems = [
    { name: "Special Masala Dosa", price: "₹50.00", badge: "VEG", time: "8 mins", emoji: "🥞" },
    { name: "Crispy Veg Burger", price: "₹65.00", badge: "POPULAR", time: "12 mins", emoji: "🍔" },
    { name: "Cold Badam Milk", price: "₹30.00", badge: "BEVERAGE", time: "3 mins", emoji: "🥛" }
  ];

  for (let i = 0; i < foodItems.length; i++) {
    const card = figma.createFrame();
    card.resize(345, 95);
    card.cornerRadius = 16;
    card.fills = solidPaint(255, 255, 255);
    card.effects = [{
      type: "DROP_SHADOW",
      color: { r: 0, g: 0, b: 0, a: 0.05 },
      offset: { x: 0, y: 4 },
      radius: 12,
      spread: 0,
      visible: true,
      blendMode: "NORMAL"
    }];
    card.x = 24;
    card.y = 310 + i * 115;

    const pic = figma.createFrame();
    pic.resize(65, 65);
    pic.cornerRadius = 12;
    pic.fills = solidPaint(254, 243, 199);
    pic.x = 15;
    pic.y = 15;
    const em = createText(foodItems[i].emoji, 28, "Bold", COLOR_DARK);
    em.x = 15;
    em.y = 15;
    pic.appendChild(em);
    card.appendChild(pic);

    const fName = createText(foodItems[i].name, 15, "Bold", COLOR_DARK);
    fName.x = 95;
    fName.y = 20;
    card.appendChild(fName);

    const fMeta = createText(foodItems[i].badge + " • ⏱ " + foodItems[i].time, 11, "Semi Bold", COLOR_ACCENT);
    fMeta.x = 95;
    fMeta.y = 44;
    card.appendChild(fMeta);

    const fPrice = createText(foodItems[i].price, 14, "Bold", COLOR_PRIMARY);
    fPrice.x = 95;
    fPrice.y = 65;
    card.appendChild(fPrice);

    const btnAdd = figma.createFrame();
    btnAdd.resize(60, 32);
    btnAdd.cornerRadius = 8;
    btnAdd.fills = solidPaint(249, 115, 22);
    btnAdd.x = 265;
    btnAdd.y = 32;
    const addLbl = createText("ADD +", 11, "Bold", rgb(255, 255, 255));
    addLbl.x = (60 - addLbl.width) / 2;
    addLbl.y = 9;
    btnAdd.appendChild(addLbl);
    card.appendChild(btnAdd);

    s2.appendChild(card);
  }

  // Floating Cart Bar
  const cartBar = figma.createFrame();
  cartBar.resize(345, 64);
  cartBar.cornerRadius = 18;
  cartBar.fills = solidPaint(15, 23, 42);
  cartBar.x = 24;
  cartBar.y = 740;
  const cartInfo = createText("2 Items in Tray • ₹80.00", 14, "Bold", rgb(255, 255, 255));
  cartInfo.x = 20;
  cartInfo.y = 22;
  cartBar.appendChild(cartInfo);
  const viewCart = createText("View Cart →", 13, "Bold", COLOR_PRIMARY);
  viewCart.x = 240;
  viewCart.y = 23;
  cartBar.appendChild(viewCart);
  s2.appendChild(cartBar);
  screens.push(s2);

  // Screen 3: Cart & Checkout
  const s3 = createScreen("03_HiFi_CartCheckout", startX + 920, 0, COLOR_BG);
  const hCart = createText("Your Tray 🛒", 22, "Bold", COLOR_DARK);
  hCart.x = 24;
  hCart.y = 70;
  s3.appendChild(hCart);

  // Bill Card
  const bill = figma.createFrame();
  bill.resize(345, 220);
  bill.cornerRadius = 20;
  bill.fills = solidPaint(255, 255, 255);
  bill.x = 24;
  bill.y = 120;
  const b1 = createText("1x Special Masala Dosa ................ ₹50.00", 13, "Medium", COLOR_DARK);
  b1.x = 20;
  b1.y = 25;
  bill.appendChild(b1);
  const b2 = createText("1x Cold Badam Milk ..................... ₹30.00", 13, "Medium", COLOR_DARK);
  b2.x = 20;
  b2.y = 60;
  bill.appendChild(b2);
  const bDiv = figma.createLine();
  bDiv.resize(305, 0);
  bDiv.x = 20;
  bDiv.y = 100;
  bDiv.strokes = solidPaint(226, 232, 240);
  bill.appendChild(bDiv);
  const bSubTot = createText("Item Total: ₹80.00", 13, "Regular", rgb(100, 116, 139));
  bSubTot.x = 20;
  bSubTot.y = 115;
  bill.appendChild(bSubTot);
  const bTax = createText("Student Canteen Subsidy: -₹0.00", 13, "Regular", COLOR_ACCENT);
  bTax.x = 20;
  bTax.y = 142;
  bill.appendChild(bTax);
  const bGrand = createText("Total Payable: ₹80.00", 16, "Bold", COLOR_DARK);
  bGrand.x = 20;
  bGrand.y = 175;
  bill.appendChild(bGrand);
  s3.appendChild(bill);

  // Pickup slot selection
  const slotCard = figma.createFrame();
  slotCard.resize(345, 90);
  slotCard.cornerRadius = 16;
  slotCard.fills = solidPaint(255, 255, 255);
  slotCard.x = 24;
  slotCard.y = 365;
  const slotLbl = createText("Preferred Pickup Time Slot", 12, "Bold", rgb(100, 116, 139));
  slotLbl.x = 20;
  slotLbl.y = 18;
  slotCard.appendChild(slotLbl);
  const slotVal = createText("⏰ 1:15 PM (Lunch Break - Slot A)", 14, "Bold", COLOR_PRIMARY);
  slotVal.x = 20;
  slotVal.y = 45;
  slotCard.appendChild(slotVal);
  s3.appendChild(slotCard);

  const btnPay = createButton("Proceed to Pay (₹80.00) →", COLOR_PRIMARY);
  btnPay.x = 24;
  btnPay.y = 740;
  s3.appendChild(btnPay);
  screens.push(s3);

  // Screen 4: Live Order Status & Token
  const s4 = createScreen("04_HiFi_LiveStatus", startX + 1380, 0, COLOR_BG);
  const hStatus = createText("Order Confirmed! 🎉", 22, "Bold", COLOR_DARK);
  hStatus.x = (393 - hStatus.width) / 2;
  hStatus.y = 80;
  s4.appendChild(hStatus);

  // Token Badge
  const tBox = figma.createFrame();
  tBox.resize(240, 170);
  tBox.cornerRadius = 24;
  tBox.fills = solidPaint(255, 255, 255);
  tBox.effects = [{
    type: "DROP_SHADOW",
    color: { r: 249/255, g: 115/255, b: 22/255, a: 0.15 },
    offset: { x: 0, y: 10 },
    radius: 25,
    spread: 0,
    visible: true,
    blendMode: "NORMAL"
  }];
  tBox.x = (393 - 240) / 2;
  tBox.y = 140;
  const tLbl = createText("CANTEEN TOKEN NUMBER", 11, "Bold", rgb(100, 116, 139));
  tLbl.x = (240 - tLbl.width) / 2;
  tLbl.y = 25;
  tBox.appendChild(tLbl);
  const tNum = createText("#B-104", 42, "Bold", COLOR_PRIMARY);
  tNum.x = (240 - tNum.width) / 2;
  tNum.y = 55;
  tBox.appendChild(tNum);
  const tSub = createText("Show this at Counter 2", 12, "Medium", COLOR_ACCENT);
  tSub.x = (240 - tSub.width) / 2;
  tSub.y = 125;
  tBox.appendChild(tSub);
  s4.appendChild(tBox);

  // Status Progress Card
  const prCard = figma.createFrame();
  prCard.resize(345, 140);
  prCard.cornerRadius = 20;
  prCard.fills = solidPaint(255, 255, 255);
  prCard.x = 24;
  prCard.y = 345;
  const prTitle = createText("Estimated Preparation Time", 12, "Bold", rgb(100, 116, 139));
  prTitle.x = 20;
  prTitle.y = 20;
  prCard.appendChild(prTitle);
  const prTime = createText("⏳ Ready in ~8 Minutes", 18, "Bold", COLOR_DARK);
  prTime.x = 20;
  prTime.y = 45;
  prCard.appendChild(prTime);

  // Progress Bar
  const pBg = figma.createFrame();
  pBg.resize(305, 8);
  pBg.cornerRadius = 4;
  pBg.fills = solidPaint(226, 232, 240);
  pBg.x = 20;
  pBg.y = 90;
  prCard.appendChild(pBg);

  const pFill = figma.createFrame();
  pFill.resize(210, 8);
  pFill.cornerRadius = 4;
  pFill.fills = solidPaint(16, 185, 129);
  pFill.x = 20;
  pFill.y = 90;
  prCard.appendChild(pFill);

  const pPct = createText("Preparing Order (70%)", 11, "Semi Bold", rgb(100, 116, 139));
  pPct.x = 20;
  pPct.y = 108;
  prCard.appendChild(pPct);
  s4.appendChild(prCard);

  const btnDone = createButton("Back to Canteen Home", COLOR_DARK, rgb(255, 255, 255));
  btnDone.x = 24;
  btnDone.y = 740;
  s4.appendChild(btnDone);
  screens.push(s4);

  // ---------------------------------------------------------------------------
  // INTERACTIVE PROTOTYPING WIRES
  // ---------------------------------------------------------------------------
  // Wire 1: btnGetStarted (Screen 1) -> Screen 2
  try {
    btnGetStarted.setReactions([
      {
        action: {
          type: 'NODE',
          destinationId: s2.id,
          navigation: 'NAVIGATE',
          transition: { type: 'SMART_ANIMATE', easing: { type: 'EASE_OUT' }, duration: 0.3 }
        },
        trigger: { type: 'ON_CLICK' }
      }
    ]);

    // Wire 2: cartBar (Screen 2) -> Screen 3
    cartBar.setReactions([
      {
        action: {
          type: 'NODE',
          destinationId: s3.id,
          navigation: 'NAVIGATE',
          transition: { type: 'SMART_ANIMATE', easing: { type: 'EASE_OUT' }, duration: 0.3 }
        },
        trigger: { type: 'ON_CLICK' }
      }
    ]);

    // Wire 3: btnPay (Screen 3) -> Screen 4
    btnPay.setReactions([
      {
        action: {
          type: 'NODE',
          destinationId: s4.id,
          navigation: 'NAVIGATE',
          transition: { type: 'SMART_ANIMATE', easing: { type: 'EASE_OUT' }, duration: 0.3 }
        },
        trigger: { type: 'ON_CLICK' }
      }
    ]);

    // Wire 4: btnDone (Screen 4) -> Screen 2
    btnDone.setReactions([
      {
        action: {
          type: 'NODE',
          destinationId: s2.id,
          navigation: 'NAVIGATE',
          transition: { type: 'SMART_ANIMATE', easing: { type: 'EASE_OUT' }, duration: 0.3 }
        },
        trigger: { type: 'ON_CLICK' }
      }
    ]);
  } catch (err) {
    // Prototyping API supported
  }

  figma.viewport.scrollAndZoomIntoView(screens);
  return { count: 4, screens: screens.map(s => s.name) };
}

// -----------------------------------------------------------------------------
// EVENT DISPATCHER
// -----------------------------------------------------------------------------
figma.ui.onmessage = async (msg) => {
  if (msg.type === 'exp12-campusbite') {
    const res = await buildExp12CampusBite();
    figma.ui.postMessage({ status: `Created ${res.count} CampusBite Wireframes!` });
  } else if (msg.type === 'exp12-booknest') {
    const res = await buildExp12BookNest();
    figma.ui.postMessage({ status: `Created ${res.count} BookNest Wireframes!` });
  } else if (msg.type === 'exp13-highfidelity') {
    const res = await buildExp13HighFidelity();
    figma.ui.postMessage({ status: `Created ${res.count} High-Fidelity Screens with Prototypes!` });
  }
};
