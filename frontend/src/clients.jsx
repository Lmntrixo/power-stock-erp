import { useState, useEffect } from "react";
const API = "http://localhost:8000/customers"

function Clients() {
    const [clients, setClients] = useState([])
    /*const [chargement, setChargement] =useState(true)*/
    const [name, setName] = useState("")
    const [email, setEmail] = useState("")
    const [telephone, setTelephone] = useState("")
    const [erreur, setErreur] = useState(null)

    function charger() {
        fetch(API)
            .then((r) => r.json())
            .then((data)=> setClients(data))
            .catch(() => {
                setErreur("impossible de joindre le serveur")
            })
    }


    useEffect(()=>{
        charger()
        /*fetch("http://localhost:8000/customers")
            .then((response) => response.json())
            .then((donnees) => {
                setClients(donnees)
                setChargement(false)
            })
            .catch(() => {
                setErreur("Impossible de joindre le serveur")
                setChargement(false)
            })*/
    },[])

    function ajouter(e) {
        e.preventDefault()
        fetch(API, {
            method: "POST",
            headers: {"content-type":"application/json"},
            body: JSON.stringify({name, email}),
        })
        .then((r) =>{
            if (!r.ok) throw new Error()
            return r.json()
        })
        .then(() => {
            setName("")
            setEmail("")
            setErreur(null)
            charger()
        })
        .catch(() => setErreur("ajout impossible"))
    }

    return (
        <div>
            <form onSubmit={ajouter} className="flex gap-2 mb-4">
                <input 
               className="border px-2 py-1 rounded"
               value={name}
               onChange={(e) => setName(e.target.value)}
               placeholder="Nom" />

                <input 
                    className="border px-2 py-1 rounded-3xl"
                    value={telephone}
                    onChange={(e) => setTelephone(e.target.value)}
                    placeholder="telephone" />
               <input
                className="border px-2 py-1 rounded"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="Email" />

                <button className="bg-blue-600 text-white px-4 py-1 rounded">Ajouter</button>
            </form>
            {erreur && <p className="text-red-600 mb-2">{erreur}</p>}

            <ul className="list-disc pl-6">
                {clients.map((c)=> (
                    <li key={c.id}>{c.name}: {c.email} : {c.telephone}/</li>
                ))}
            </ul>
        </div>
    )

    /*if (chargement) return  <p>Chargement.....</p>
    if (erreur) return <p className="text-red-600">{erreur}</p>

    return (
        <ul className="list-disc pl-6 flex-4">
            {clients.map((client)=> (
                <li key={client.id}>{client.name}</li>
            ))}

        </ul>
    )*/
}

export default Clients

