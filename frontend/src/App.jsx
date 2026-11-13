import { useState } from "react"
import Menu from "./menu"
import Taches from "./form"
import Clients from "./clients"
import { Routes, Route, Link } from "react-router-dom"

function Visible(){
  const [visible, SetVisible] = useState(true)
  return (
    <div className="p-4">
      <button
        className="bg-blue-600 text-white px-4 py-2 rounded"
        onClick={() => SetVisible(!visible)}>
          {visible ? "Masquer": "Afficher"}
      </button>
      {visible && <p className="mt-4"> Bonjour Evans</p>}
    </div>
  )
}
function Compteur (){
  const [compte, setCompte] = useState(0)
  return(
    <div className="p-4">
      <p className="text-xl">Clics : {compte}</p>
      <button 
        className="bg-blue-600 text-white px-4 py-2 rounded"
        onClick={() => setCompte(compte +1)}>
          cliquer 
      </button>
      <div>
        <button
        className="py-5 px-4 my-5"
        onClick={()=> setCompte(0)}>
        reinitialiser
      </button>
      </div>

      <div>
        <button
        className="py-5 px-4 my-5"
        onClick={()=> setCompte(compte-1)}>
        dimunuer
      </button>
      </div>
    </div>
  )
}

function Bonjour(){
  const nom = "Evans"
  return <h1 className="text-3xl font-bold text-blue-600"> Bonjour {nom}</h1>
}
function Card(props){
 /* const title = "le titre du film"
  const sentence = "ceci est une phrase"**/

  return <div className="border p-4 rounded-3xl">
    <h2 className="font-bold">{props.title}</h2>
    <p>{props.sentence}</p>
    <p>{props.niveau}</p>
  </div>
}

function Accueil(){
  return <h1 className="text-2xl font-bold">Accueil</h1>
}
function App(){
  return (
    <div className="p-6 space-y-4">
      <nav className="flex gap-4 mb-6">
        <Link to="/" className="text-blue-600">Accueil</Link>
        <Link to="/clients" className="text-blue-600">Clients</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Accueil />} />
        <Route path="/clients" element={<Clients />} />
      </Routes>
      <Visible />
      <Compteur />
      <Bonjour />
      <Bonjour />
      <Card title="React Js" sentence="le framework frontend le plus utilse" niveau={3}/>
      <Card title="FastAPI" sentence=" le framework backend le plus rapide" niveau={5}/>
      <Card title="Postgres" sentence="la base de donnees la plus utilisee" niveau={4}/>
      <Menu />
      <Taches />
    </div>
  )
}

export default App ;Visible;