// async, await
const axios = require("axios");

console.log("■ 서울시 지하철 승하차 인원 정보 ■");

const api_key = "484e536751686d6336306d484d7576";

// 비동기 작업을 순차적으로 진행하려면?

async function print(date) {
  console.log('👩', date, '👩');
  url = `http://openapi.seoul.go.kr:8088/${api_key}/json/CardSubwayStatsNew/1/5/${date}`;

  const { data } = await axios.get(url);
  printResult(data)
}

// print('20260601');
// print('20260602');
// print('20260603');
// 만약 이를 순차적(동기) 로 진행하려면?
print('20260601')
  .then(() => print('20260602'))
  .then(() => print('20260603'))
  ;

function printResult(jsObj) {
  const table = [];
  table.push("호선 | 역명 | 승차인원 | 하차인원");
  for (row of jsObj.CardSubwayStatsNew.row) {
    table.push(`${row.SBWY_ROUT_LN_NM}|${row.SBWY_STNS_NM}|${row.GTON_TNOPE}|${row.GTOFF_TNOPE}`);
  }
  console.log(table.join('\n'));
}

// 비동기 실행 확인
console.log("👧", "언제 찍힐까?", "👨");
