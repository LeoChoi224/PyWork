// 성이 '김' 씨인 사람만 담긴 배열 구하기
const students = [
    {name: '김철수', score: [10, 20, 30]},
    {name: '박수진', score: [90, 33, 56]},
    {name: '김영희', score: [45, 78, 31]},
    {name: '조수현', score: [99, 100, 67]},
]
Object.freeze(students);  // 원본 변화시키지 말기

function filterObj(data, start){

    TODO

}
console.log(filterObj(students, '김'));
// 결과 ↓ 
// [
//     { name: '김철수', score: [ 10, 20, 30 ] },
//     { name: '김영희', score: [ 45, 78, 31 ] }
// ]
