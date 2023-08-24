fetch("http://127.0.0.1:5000/predict/104/18/33/23.603016/60.3/6.7/140.91").then((res)=>{
    res.json().then(console.log(res));
})