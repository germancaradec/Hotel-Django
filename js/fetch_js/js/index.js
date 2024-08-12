const CONSULTAS_URL = "http://127.0.0.1:8000/contacto/consultas/"

let consultas = null

const getConsultas = async()=>{
    const res=await fetch(CONSULTAS_URL)
    const data=await res.json()
    console.log(data)
    consultas = data.consultas
    console.log(consultas)
}

window.addEventListener("load", function () {
    getConsultas()
})