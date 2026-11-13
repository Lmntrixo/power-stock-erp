/*import { useState } from "react";*/

function Languages() {
    const langages = ["python", "Javascript", "PHP"]
     return (
        <ul className="list-disc pl-6">
            {langages.map((langage) => (
                <li key={langage}>{langage}</li>
            ))}
        </ul>
     )
}

export default Languages