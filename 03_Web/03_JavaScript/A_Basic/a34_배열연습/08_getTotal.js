// 총점을 담은 배열 생성하기
const students = [
    {name: '김철수', score: [10, 20, 30]},
    {name: '박수진', score: [90, 33, 56]},
    {name: '김영희', score: [45, 78, 31]},
    {name: '조수현', score: [99, 100, 67]},
]
Object.freeze(students); // ※ 원본 배열 students 는 건드리지 말고 새로운 배열로 생성하여 리턴하세요

function getTotal(data){

    


}
console.log(getTotal(students));

// 결과] ↓
// [
//     { name: '김철수', total: 60 },      
//     { name: '박수진', total: 179 },     
//     { name: '김영희', total: 154 },     
//     { name: '조수현', total: 266 }      
// ]    
