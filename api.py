<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>LIPZX STORE</title>

<style>
body {
  margin: 0;
  font-family: Arial;
  background: #050b18;
  color: white;
}

/* HEADER */
.header {
  text-align: center;
  padding: 20px;
}

.header h1 {
  margin: 0;
  font-size: 26px;
}

.header h2 {
  margin: 10px 0 0;
  font-size: 22px;
}

.sub {
  color: #38bdf8;
  font-size: 12px;
  letter-spacing: 2px;
}

/* TAB */
.tabs {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin: 20px 0;
}

.tab {
  padding: 8px 18px;
  border-radius: 20px;
  background: #111827;
  color: #aaa;
  cursor: pointer;
}

.tab.active {
  background: #38bdf8;
  color: black;
  box-shadow: 0 0 15px #38bdf8;
}

/* READY */
.ready {
  padding: 10px 20px;
  font-size: 12px;
  color: #aaa;
  letter-spacing: 2px;
}

/* GRID */
.container {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  padding: 10px;
}

/* CARD */
.card {
  background: #0f172a;
  border-radius: 12px;
  padding: 12px;
  text-align: center;
  position: relative;
  overflow: hidden;
}

/* garis atas */
.card::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 4px;
}

.basic::before { background: #22c55e; }
.rare::before { background: #38bdf8; }
.epic::before { background: #a855f7; }

/* label */
.label {
  font-size: 10px;
  color: #aaa;
  margin-bottom: 5px;
}

.id {
  font-size: 14px;
}

.price {
  color: gold;
  margin: 5px 0;
}

/* BUTTON */
.btn {
  background: #e5e5e5;
  color: black;
  padding: 8px;
  border-radius: 8px;
  text-decoration: none;
  display: block;
  margin-top: 8px;
}

/* SOLD */
.sold {
  opacity: 0.5;
  filter: grayscale(1);
  pointer-events: none;
}

.sold::after {
  content: "SOLD";
  position: absolute;
  top: 40%;
  left: 50%;
  transform: translate(-50%, -50%);
  background: red;
  color: white;
  padding: 5px 12px;
  border-radius: 8px;
  font-size: 12px;
  font-weight: bold;
}

/* POPUP QR */
.payment {
  position: fixed;
  bottom: -100%;
  left: 0;
  width: 100%;
  background: #0f172a;
  padding: 20px;
  border-radius: 20px 20px 0 0;
  text-align: center;
  transition: 0.3s;
}

.payment.active {
  bottom: 0;
}

.payment img {
  width: 200px;
  border-radius: 10px;
}

.konfirmasi {
  background: #22c55e;
  color: white;
}
</style>
</head>

<body>

<div class="header">
  <h1>LIPZX STORE</h1>
  <h2>FF ID CANTIK</h2>
  <div class="sub">PENYETOKNYA ID CANTIK</div>
</div>

<div class="tabs">
  <div class="tab active" onclick="filter('all', this)">Semua</div>
  <div class="tab" onclick="filter('basic', this)">Basic</div>
  <div class="tab" onclick="filter('rare', this)">Rare</div>
  <div class="tab" onclick="filter('epic', this)">Epic</div>
</div>

<div class="ready">READY STOCK</div>

<div class="container">

<!-- NORMAL -->

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15218199990</div>
  <div class="price">Rp10.000</div>
  <a class="btn" onclick="beli('15218199990','10.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15220055556</div>
  <div class="price">Rp10.000</div>
  <a class="btn" onclick="beli('15220055556','10.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15251200009</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15251200009','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15259900002</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15259900002','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15255950000</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15255950000','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15260000747</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15260000747','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15260000533</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15260000533','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15260000499</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15260000499','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15260000455</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15260000455','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15260000950</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15260000950','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15538816666</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15538816666','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15538669999</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15538669999','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15379000804</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15379000804','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15379000805</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15379000805','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15380000780</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15380000780','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15371299999</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15371299999','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15375999997</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15375999997','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15371088888</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15371088888','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15324444443</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15324444443','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15333022227</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15333022227','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15333022225</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15333022225','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15333374474</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15333374474','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15300200403</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15300200403','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15300300104</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15300300104','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15303000904</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15303000904','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15476600600</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15476600600','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15300060027</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15300060027','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15301900006</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15301900006','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15302400003</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15302400003','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15378888853</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15378888853','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15377777117</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15377777117','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15377772737</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15377772737','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15377772177</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15377772177','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15376900000</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15376900000','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15259999896</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15259999896','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15228909999</div>
  <div class="price">Rp15.000</div>
  <a class="btn" onclick="beli('15228909999','15.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15344337777</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15344337777','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15344442244</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15344442244','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15410909999</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15410909999','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15538600006</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15538600006','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15266666996</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15266666996','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15344462222</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15344462222','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15355578888</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15355578888','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15366866663</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15366866663','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15258888484</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15258888484','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15259333336</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15259333336','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15254955555</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15254955555','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15251777772</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15251777772','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15245277777</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15245277777','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15241555556</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15241555556','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15255557707</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15255557707','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15077377772</div>
  <div class="price">Rp20.000</div>
  <a class="btn" onclick="beli('15077377772','20.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15533999889</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15533999889','25.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15522443323</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15522443323','25.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15534448884</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15534448884','25.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15533886662</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15533886662','25.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15533887774</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15533887774','25.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15550088003</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15550088003','25.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15555229992</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15555229992','25.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15533888448</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15533888448','25.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15566444553</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15566444553','25.000')">BELI</a>
</div>

<div class="card basic">
  <div class="label">BASIC</div>
  <div class="id">15566441110</div>
  <div class="price">Rp25.000</div>
  <a class="btn" onclick="beli('15566441110','25.000')">BELI</a>
</div>

<!-- SOLD -->
<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15269999006</div>
  <div class="price">Rp5.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15374333300</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15266055557</div>
  <div class="price">Rp5.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15220222274</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15220929999</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15229000014</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15222300002</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15222250222</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15239793333</div>
  <div class="price">Rp5.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15229000067</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15340020000</div>
  <div class="price">Rp20.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15544300003</div>
  <div class="price">Rp20.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card basic sold">
  <div class="label">BASIC</div>
  <div class="id">15344444456</div>
  <div class="price">Rp20.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15522333311</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15522333311','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15550055225</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15550055225','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15533884444</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15533884444','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15533990044</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15533990044','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15522444499</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15522444499','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15566114488</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15566114488','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15566668800</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15566668800','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15568500000</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15568500000','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15555229996</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15555229996','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15555229990</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15555229990','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15544446662</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15544446662','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15399993998</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15399993998','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15400144444</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15400144444','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15400090999</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15400090999','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15411000090</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15411000090','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15388886600</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15388886600','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15402226666</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15402226666','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15378888988</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15378888988','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15222298999</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15222298999','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15222255595</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15222255595','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15222323323</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15222323323','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15239898888</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15239898888','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15477333303</div>
  <div class="price">Rp30.000</div>
  <a class="btn" onclick="beli('15477333303','30.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15568800000</div>
  <div class="price">Rp35.000</div>
  <a class="btn" onclick="beli('15568800000','35.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15233330030</div>
  <div class="price">Rp40.000</div>
  <a class="btn" onclick="beli('15233330030','40.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15555553311</div>
  <div class="price">Rp40.000</div>
  <a class="btn" onclick="beli('15555553311','40.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15554000003</div>
  <div class="price">Rp40.000</div>
  <a class="btn" onclick="beli('15554000003','40.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15266060000</div>
  <div class="price">Rp40.000</div>
  <a class="btn" onclick="beli('15266060000','40.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15266000006</div>
  <div class="price">Rp40.000</div>
  <a class="btn" onclick="beli('15266000006','40.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15222255155</div>
  <div class="price">Rp40.000</div>
  <a class="btn" onclick="beli('15222255155','40.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15555000040</div>
  <div class="price">Rp45.000</div>
  <a class="btn" onclick="beli('15555000040','45.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15266666880</div>
  <div class="price">Rp45.000</div>
  <a class="btn" onclick="beli('15266666880','45.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15260000404</div>
  <div class="price">Rp45.000</div>
  <a class="btn" onclick="beli('15260000404','45.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15266444422</div>
  <div class="price">Rp45.000</div>
  <a class="btn" onclick="beli('15266444422','45.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15389999009</div>
  <div class="price">Rp55.000</div>
  <a class="btn" onclick="beli('15389999009','55.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15399222223</div>
  <div class="price">Rp55.000</div>
  <a class="btn" onclick="beli('15399222223','55.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15388188885</div>
  <div class="price">Rp55.000</div>
  <a class="btn" onclick="beli('15388188885','55.000')">BELI</a>
</div>

<div class="card rare">
  <div class="label">RARE</div>
  <div class="id">15386566666</div>
  <div class="price">Rp55.000</div>
  <a class="btn" onclick="beli('15386566666','55.000')">BELI</a>
</div>

<div class="card rare sold">
  <div class="label">RARE</div>
  <div class="id">15440777713</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card rare sold">
  <div class="label">RARE</div>
  <div class="id">15400022225</div>
  <div class="price">Rp30.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card rare sold">
  <div class="label">RARE</div>
  <div class="id">15566448899</div>
  <div class="price">Rp30.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card rare sold">
  <div class="label">RARE</div>
  <div class="id">15244881111</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card rare sold">
  <div class="label">RARE</div>
  <div class="id">15400003636</div>
  <div class="price">Rp40.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card rare sold">
  <div class="label">RARE</div>
  <div class="id">15269998882</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card rare sold">
  <div class="label">RARE</div>
  <div class="id">15229393939</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card rare sold">
  <div class="label">RARE</div>
  <div class="id">15229191918</div>
  <div class="price">Rp10.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card rare sold">
  <div class="label">RARE</div>
  <div class="id">15555000010</div>
  <div class="price">Rp45.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15400003010</div>
  <div class="price">Rp60.000</div>
  <a class="btn" onclick="beli('15400003010','60.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15700000170</div>
  <div class="price">Rp60.000</div>
  <a class="btn" onclick="beli('15700000170','60.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15700000580</div>
  <div class="price">Rp60.000</div>
  <a class="btn" onclick="beli('15700000580','60.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15699999019</div>
  <div class="price">Rp60.000</div>
  <a class="btn" onclick="beli('15699999019','60.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15699999934</div>
  <div class="price">Rp60.000</div>
  <a class="btn" onclick="beli('15699999934','60.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15699999660</div>
  <div class="price">Rp60.000</div>
  <a class="btn" onclick="beli('15699999660','60.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15699999040</div>
  <div class="price">Rp60.000</div>
  <a class="btn" onclick="beli('15699999040','60.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15699999440</div>
  <div class="price">Rp60.000</div>
  <a class="btn" onclick="beli('15699999440','60.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15400006009</div>
  <div class="price">Rp60.000</div>
  <a class="btn" onclick="beli('15400006009','60.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15300600008</div>
  <div class="price">Rp65.000</div>
  <a class="btn" onclick="beli('15300600008','65.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15402000070</div>
  <div class="price">Rp65.000</div>
  <a class="btn" onclick="beli('15402000070','65.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15677777787</div>
  <div class="price">Rp70.000</div>
  <a class="btn" onclick="beli('15677777787','70.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15700000069</div>
  <div class="price">Rp70.000</div>
  <a class="btn" onclick="beli('15700000069','70.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15700000079</div>
  <div class="price">Rp70.000</div>
  <a class="btn" onclick="beli('15700000079','70.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15700000084</div>
  <div class="price">Rp70.000</div>
  <a class="btn" onclick="beli('15700000084','70.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15700006666</div>
  <div class="price">Rp70.000</div>
  <a class="btn" onclick="beli('15700006666','70.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15378888888</div>
  <div class="price">Rp80.000</div>
  <a class="btn" onclick="beli('15378888888','80.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15700003000</div>
  <div class="price">Rp80.000</div>
  <a class="btn" onclick="beli('15700003000','80.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15555552525</div>
  <div class="price">Rp80.000</div>
  <a class="btn" onclick="beli('15555552525','80.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15555556600</div>
  <div class="price">Rp90.000</div>
  <a class="btn" onclick="beli('15555556600','90.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15544444411</div>
  <div class="price">Rp100.000</div>
  <a class="btn" onclick="beli('15544444411','100.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15544444111</div>
  <div class="price">Rp100.000</div>
  <a class="btn" onclick="beli('15544444111','100.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15555566662</div>
  <div class="price">Rp125.000</div>
  <a class="btn" onclick="beli('15555566662','125.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15555566663</div>
  <div class="price">Rp125.000</div>
  <a class="btn" onclick="beli('15555566663','125.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15544444447</div>
  <div class="price">Rp125.000</div>
  <a class="btn" onclick="beli('15544444447','125.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15677777771</div>
  <div class="price">Rp125.000</div>
  <a class="btn" onclick="beli('15677777771','125.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15677777772</div>
  <div class="price">Rp125.000</div>
  <a class="btn" onclick="beli('15677777772','125.000')">BELI</a>
</div>

<div class="card epic">
  <div class="label">EPIC</div>
  <div class="id">15300000010</div>
  <div class="price">Rp1.000.000</div>
  <a class="btn" onclick="beli('15300000010','1.000.000')">BELI</a>
</div>

<div class="card epic sold">
  <div class="label">EPIC</div>
  <div class="id">15677777777</div>
  <div class="price">Rp350.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card epic sold">
  <div class="label">EPIC</div>
  <div class="id">15515155551</div>
  <div class="price">Rp90.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card epic sold">
  <div class="label">EPIC</div>
  <div class="id">15700000057</div>
  <div class="price">Rp70.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card epic sold">
  <div class="label">EPIC</div>
  <div class="id">15700000087</div>
  <div class="price">Rp70.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card epic sold">
  <div class="label">EPIC</div>
  <div class="id">15700000045</div>
  <div class="price">Rp70.000</div>
  <a class="btn">SOLD</a>
</div>

<div class="card epic sold">
  <div class="label">EPIC</div>
  <div class="id">15700000058</div>
  <div class="price">Rp70.000</div>
  <a class="btn">SOLD</a>
</div>

</div>

<!-- QR -->
<div class="payment" id="pay">
  <h2>Pembayaran QRIS</h2>
  <p id="info"></p>

  <img src="qr.png">

  <p>Scan QR lalu kirim bukti</p>

  <a id="wa" class="btn konfirmasi">Konfirmasi ke Admin</a>
  <a class="btn" onclick="tutup()">Kembali</a>
</div>

<script>
function filter(type, el){
  let cards = document.querySelectorAll('.card');
  let tabs = document.querySelectorAll('.tab');

  tabs.forEach(t => t.classList.remove('active'));
  el.classList.add('active');

  cards.forEach(c => {
    if(type === 'all'){
      c.style.display = 'block';
    } else {
      c.style.display = c.classList.contains(type) ? 'block' : 'none';
    }
  });
}

function beli(id, harga){
  document.getElementById("pay").classList.add("active");
  document.getElementById("info").innerText =
    "ID: " + id + " | Rp" + harga;

  document.getElementById("wa").href =
    "https://wa.me/6283822416101?text=Saya sudah bayar ID " + id + " Rp" + harga + ", ini bukti transfer";
}

function tutup(){
  document.getElementById("pay").classList.remove("active");
}
</script>

</body>
</html>
