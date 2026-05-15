// JSON 데이터 받기
/*
■서울시 지하철호선별 역별 승하차 인원 정보 
http://data.seoul.go.kr/dataList/datasetView.do?infId=OA-12914&srvType=A&serviceKind=1&currentPageNo=1
*/
const axios = require("axios");

console.log("■ 서울시 지하철 승하차 인원 정보 ■");

const date = "20240701";
const api_key = "당신의 KEY 값은?";

url = `http://openapi.seoul.go.kr:8088/${api_key}/json/CardSubwayStatsNew/1/5/${date}`;

// TODO

// 비동기 실행 확인
console.log("👧", "언제 찍힐까?", "👨");
