// JSON 데이터 받기
/*
■서울시 지하철호선별 역별 승하차 인원 정보 
http://data.seoul.go.kr/dataList/datasetView.do?infId=OA-12914&srvType=A&serviceKind=1&currentPageNo=1
*/
const axios = require("axios");

console.log("■ 서울시 지하철 승하차 인원 정보 ■");

const date = "20260601";
const api_key = "484e536751686d6336306d484d7576";

url = `http://openapi.seoul.go.kr:8088/${api_key}/json/CardSubwayStatsNew/1/5/${date}`;

axios.get(url)
    .then(response => {
        // console.log(response.data);
        printResult(response.data);
    })


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
