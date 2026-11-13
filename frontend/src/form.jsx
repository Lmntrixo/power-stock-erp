import { useState } from "react";

function Taches(){
    const [texte, setTexte] = useState("")
    const [taches, setTaches] = useState([])

    function ajouter(e) {
        e.preventDefault()
        if (texte.trim() === "") return
        setTaches([...taches, texte])
        setTexte("")
    }

    return (
    <div className="p-4">
        <form action="" method="" onSubmit={ajouter} className="flex gap-2">
            <input
             type=""
             className="border px-2 py-1 rounded"
             value={texte}
             onChange={(e) => setTexte(e.target.value)}
             placeholder="Nouvelle tache"
             />
             <button className="bg-blue-600 text-white px-4 py-1 rounded">
                Ajouter
             </button>
        </form>
        <ul className="mt-4 list-disc pl-6">
            {taches.map((tache,index) => (
                <li key={index}>{tache}</li>
            ))}
        </ul>

    </div>
)
}

export default Taches

