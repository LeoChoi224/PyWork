// XML 데이터 받기

/**
 * DOMParser 와 같은 객체는 Node.js 환경에서 제공되진 않는다
 * 
 * 
 * Node.js 에서 xml 파싱 참조:
 *   https://stackoverflow.com/questions/11398419/trying-to-use-the-domparser-with-node-js
 */

/*
■서울시 지하철호선별 역별 승하차 인원 정보 
http://data.seoul.go.kr/dataList/datasetView.do?infId=OA-12914&srvType=A&serviceKind=1&currentPageNo=1
*/
const axios = require("axios");

// npm install @xmldom/xmldom  설치
const { DOMParser } = require('@xmldom/xmldom');

console.log("■ 서울시 지하철 승하차 인원 정보 ■");

const date = "20260601";
const api_key = "484e536751686d6336306d484d7576";

url = `http://openapi.seoul.go.kr:8088/${api_key}/xml/CardSubwayStatsNew/1/5/${date}`;

axios.get(url)
    .then(response => {
        // console.log(response.data)  // xml 응답은 string 으로 받아온다.

        const domParser = new DOMParser();
        const xmlDom = domParser.parseFromString(response.data, 'application/xml');
        printXML(xmlDom);
    })


function printXML(xmlDOM) {
  const table = [];
  table.push("호선 | 역명 | 승차인원 | 하차인원");

  for(row of xmlDOM.getElementsByTagName("row")){
		table.push(
			row.getElementsByTagName("SBWY_ROUT_LN_NM")[0].childNodes[0].nodeValue + "|" + 
			row.getElementsByTagName("SBWY_STNS_NM")[0].childNodes[0].nodeValue + "|" + 
			row.getElementsByTagName("GTON_TNOPE")[0].childNodes[0].nodeValue + "|" + 
			row.getElementsByTagName("GTOFF_TNOPE")[0].childNodes[0].nodeValue 
		);
	}

  console.log(table.join('\n'));
}


// 비동기 실행 확인
console.log("👧", "언제 찍힐까?", "👨");
