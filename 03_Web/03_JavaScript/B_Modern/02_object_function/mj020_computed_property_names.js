/**
 * computed property names
 * 
 *  https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names
 * 
 * 
 *  object initializer syntax 에서는 computed property names 를 지원한다
 *  object property 에 [..] 사용하여 계산된 결과값으로 object property 지정 가능 
 */

// 과연 아래와 같은 것이 가능할까?
{
  let [name1, name2, name3] = ["a", "b", "c"];

  const obj1 = {
    name1: "alpha",
    name2: "beta",
    name3: "gamma",
  };

  // 과연 이렇게 만들어졌을까?
  // --> { a: 'alpha', b: 'beta', c: 'gamma' } ?

  console.log("obj1 =", obj1);  // { name1: 'alpha', name2: 'beta', name3: 'gamma' }

  // computed property names 를 사용하면
  // 수식 결과를 key 값으로 사용 가능!

  const obj2 = {
    [name1]: "alpha",
    [name2]: "beta",
    [name3]: "gamma",    
  }
  console.log('obj2 =', obj2);

}


{
  let i = 0;
  console.log({
    [`foo`]: i,
    [`foo`]: i,
    [`foo`]: i,
  });
}




