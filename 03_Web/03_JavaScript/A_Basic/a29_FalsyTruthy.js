/*
    조건문 : Conditional Statements 에서

    거짓(Falsy) 으로 평가될때!
        false, 0, '', null, undefined, NaN   <-- 'Falsy 한 값'이라 한다

    참(Truthy) 으로 평가될때
        true, 37, 'Mark', {}, [], Infinity   <-- 'Truthy 한 값' 이라 한다

    https://developer.mozilla.org/ko/docs/Glossary/Truthy
    https://developer.mozilla.org/ko/docs/Glossary/Falsy

*/
function print(data){
    if(data)  // ← Truthy, Falsy 판정
        console.log(data, '-- Truthy 판정');
    else
        console.log(data, '-- Falsy 판정');
}

print(false);
print(0);
print(0.0);
print('');
print(null);
print(undefined);
print(NaN);

console.log();

print(true);
print(-37);
print('신하석');
print(' ');
print({성: '신', 이름: '하석'});
print([10, 20, 30]);
print({});
print([]);
print(Infinity);


