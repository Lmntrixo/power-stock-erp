import { useState } from "react";

function AfficheMenu (){
    const [visible, setVisible] = useState(true)

    return (
        <div className="p-4 rounded-3xl">
            <button
            className="px-4 py-4 text-white"
            onClick={() => setVisible(!visible)}
            >{visible ? "Masquer":"Afficher"}
            </button>
            {visible && <ul className="mx-5 my-5 px-5 py-5">
                <li>apprendre FastAPi</li>
                <li>apprendre Laravel</li>
                <li>apprende ReactJs</li>
                </ul>
            }

        </div>
    )
}

function Menu(){
    return (
        <AfficheMenu />
    )
}

export default Menu
