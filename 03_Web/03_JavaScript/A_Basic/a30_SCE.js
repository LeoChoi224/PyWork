// &&, || 연산자에 대해 생각해보자

let result;

function print(data){
    if(data)  // ← Truthy, Falsy 판정
        console.log(data, '-- Truthy 판정');
    else
        console.log(data, '-- Falsy 판정');
}

print(true && false);
print(true || false);

print(true && 'hello');
print(0 && 'hello');

print(null || '기본값');
print(undefined || '기본값');

/*****************************************
 * SCE 는 
 * React 등에서 '조건부 렌더링' 등을 할때 많이 사용하는 문법이다
 * 특정 값이 유효할때만 수행해야 하는 상황
 */
console.log('-'.repeat(20));

getName = function(animal){
    return animal.name;
};

dog = {name: '검둥이'};
console.log(getName(dog));

// dog = null;
// console.log(getName(dog));

dog = {age: 12};
console.log(getName(dog));

// SCE 로 매개변수 검증
getName = function(animal) {
    const name = animal && animal.name;
    return name || '이름이 없는 동물';
}

dog = null;
console.log(getName(dog));

dog = {age: 12};
console.log(getName(dog));

