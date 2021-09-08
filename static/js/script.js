
setInterval(()=>{
    let myDate = new Date();
    ah = myDate.getHours(); 
    am = myDate.getMinutes(); 
    ase = myDate.getSeconds();
    myt = ah+":"+am+":"+ase
    //document.write(myt)
    document.getElementById('time').innerHTML=ah+":"+am+":"+ase;
},1000);