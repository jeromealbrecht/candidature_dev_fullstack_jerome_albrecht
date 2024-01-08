function genererTourMagique() {
    fetch('/api/generer_tour_magique')
        .then(response => response.json())
        .then(data => {
            document.getElementById('tourMagique').textContent = data.tour_magique;
        })
        .catch(error => console.error('Erreur lors de la récupération du tour magique :', error));
}

function toggleProfile() {
    let profileSection = document.getElementById("profileSection");
    if (profileSection.style.display === "flex" || profileSection.style.display === "") {
        profileSection.style.display = "none";
    } else {
        profileSection.style.display = "flex";
    }
}

function toggleLetter() {
    let letterSection = document.getElementById("letterSection");
    if (letterSection.style.display === "flex" || letterSection.style.display === "") {
        letterSection.style.display = "none";
    } else {
        letterSection.style.display = "flex";
    }
}

function toggleAbout() {
    let presenceDoc = document.getElementById("presenceDoc");
    if (presenceDoc.style.display === "flex" || presenceDoc.style.display === "") {
        presenceDoc.style.display = "none";
    } else {
        presenceDoc.style.display = "flex";
    }
}