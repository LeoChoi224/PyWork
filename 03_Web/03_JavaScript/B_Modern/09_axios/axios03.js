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

console.log("■ 서울시 지하철 승하차 인원 정보 ■");

const date = "20240701";
const api_key = "너의 키값은?";

url = `http://openapi.seoul.go.kr:8088/${api_key}/xml/CardSubwayStatsNew/1/5/${date}`;

// TODO

// 비동기 실행 확인
console.log("👧", "언제 찍힐까?", "👨");
