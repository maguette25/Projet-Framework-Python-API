const students = [
  { num: "2014079LH", nom: "CISSE", prenom: "Baba", classe: "6ème A", moy: 10.8, source: "A.P", validite: "Valide" },
  { num: "2015123KD", nom: "NDIAYE", prenom: "Awa", classe: "5ème B", moy: 12.4, source: "A.P", validite: "Valide" },
  { num: "20140562YT", nom: "DIARRA", prenom: "Alius", classe: "4ème C", moy: 13.2, source: "A.P", validite: "Valide" },
];

const table = document.getElementById("studentTable");

students.forEach(s => {
  const row = document.createElement("tr");
  if (s.validite === "Invalide") row.classList.add("invalid");
  row.innerHTML = `
    <td>${s.num}</td><td>${s.nom}</td><td>${s.prenom}</td>
    <td>${s.classe}</td><td>${s.moy}</td><td>${s.source}</td>
    <td>${s.validite}</td>
    <td><button>Archiver</button> <button>Supprimer</button></td>
  `;
  table.appendChild(row);
});