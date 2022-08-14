function createModal(origin_src) {
    let coverModal = document.getElementById("cover-div-global");
    if (coverModal !== null) {
        coverModal.remove();
    }

    coverModal = document.createElement("div");
    coverModal.id = "cover-div-global";
    coverModal.innerHTML = `
        <div id="cover-div"></div>
        <div id="cover-container"><div id="cover-photo"><img src="" alt="Пост" id="BigSizePhoto"></div></div>
        <div id="cover-exit"><div id="cross-exit"><i class="fa-solid fa-xmark"></i></div></div>`;

    document.body.style.overflowY = "hidden";
    document.body.append(coverModal);
    document.getElementById("BigSizePhoto").src = origin_src; // "http://drive.google.com/uc?export=view&id=1iw2yepgodB0n5lglh7EThnbwx-JPNJvF";
}

function removeModal() {
    document.getElementById("cover-div-global").remove();
}

const showFull = (origin_src) => {
    createModal(origin_src);
    let clickPhoto = 0;
    let clickOut = 0;

    function complete() {
        document.getElementById("cover-container").style.display = "none";
        document.getElementById("cover-exit").style.display = "none";
        document.body.style.overflowY = "";
        removeModal();
    }

    document.onkeydown = function (e) {
        if (e.key == "Escape") {
            complete();
        }
    }

    document.getElementById("cover-exit").onclick = function () {
        complete();
    }

    document.getElementById("BigSizePhoto").onclick = function () {
        clickPhoto = 1;
    }

    document.getElementById("cover-container").onclick = function () {
        clickOut = 1;
        if (clickOut && !clickPhoto) {
            clickOut = 0;
            complete();
        }
        clickPhoto = 0;
    }
}

if (window.innerWidth >= 1300) {
    for (let i = 1; i <= 10; i++) {
        let photoPost = document.getElementById("img-" + i);
        if (photoPost !== null) {
            photoPost.onclick = function () {
                showFull(photoPost.src);
            };
        } else break;
    }
}
if (window.innerWidth < 800) {
    for (let i = 1; i <= 10; i++) {
        let photoPost = document.getElementById("img-" + i);
        if (photoPost !== null) {
            photoPost.style.height = "17em";
            photoPost.style.width = "fit-content";

        }
    }
}
