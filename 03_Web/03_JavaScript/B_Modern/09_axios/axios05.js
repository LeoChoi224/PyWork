const axios = require("axios");

const url = "https://httpbingo.org/get";

// axios.get(url, {params: {name: '김정준', age: 34}})
//     .then(response => {
//         console.log(response.data);
//     })

async function action(name) {
    const { data } = await axios.get(url, { params: { name } });
    console.log(data.args.name)
}

// 결과 순서가 보장 안됨
// action('박영진');
// action('김정준');
// action('박수연');
// action('홍묵이');

(async function() {
    await action('박영진');
    await action('김정준');
    await action('박수연');
    await action('홍묵이');
})()