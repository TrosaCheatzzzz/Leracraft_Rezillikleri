function carousel() {
    return {
        active: 0,
        flkty: null,
        init() {
            this.flkty = new Flickity(this.$refs.carousel, {
                wrapAround: true,
                pageDots: false,
                prevNextButtons: false
            });
            this.flkty.on('change', i => this.active = i);
        },
        previousSlide() {
            this.flkty.previous(true);
        },
        nextSlide() {
            this.flkty.next(true);
        }
    }
}

function body() {
    return {
        modals: false,
        previousModalName: null,
        toggleModal(modalName) {
            const modal = this.$refs[modalName].style;
            this.modals = !this.modals;
            if (modal.display === 'none') {
                modal.display = 'block';
            } else {
                modal.display = 'none';
            }

            if (this.previousModalName !== null) {
                const previousModal = this.$refs[this.previousModalName].style;
                if (previousModal.display === 'none') {
                    previousModal.display = 'block';
                } else {
                    previousModal.display = 'none';
                }
            }
            this.previousModalName = modalName;
        },
        closeModal() {
            this.modals = false;
            if (this.previousModalName !== null) {
                const previousModal = this.$refs[this.previousModalName].style;
                if (previousModal.display === 'none') {
                    previousModal.display = 'block';
                } else {
                    previousModal.display = 'none';
                }
            }
        },
        dropdown(templateName) {
            return {
                content: () => this.$refs[templateName].innerHTML,
                allowHTML: true,
                appendTo: this.$root
            }
        }
    }
}

function rgbToHex(rgb) {
    let hex = Number(rgb).toString(16);
    if (hex.length < 2) {
        hex = "0" + hex;
    }
    return hex;
}

let color = getComputedStyle(document.documentElement).getPropertyValue('--voonos-emerald-100');
color = color.trim().split(' ')
color = '#' + rgbToHex(color[0]) + rgbToHex(color[1]) + rgbToHex(color[2])
particlesJS("particles-js", {
    "particles": {
        "number": {"value": 150, "density": {"enable": true, "value_area": 3000}},
        "color": {"value": color},
        "shape": {
            "type": "circle",
            "stroke": {"width": 0, "color": "#000000"},
            "polygon": {"nb_sides": 3},
            "image": {"src": "img/github.svg", "width": 200, "height": 200}
        },
        "opacity": {
            "value": 0.5,
            "random": true,
            "anim": {"enable": false, "speed": 1, "opacity_min": 0.1, "sync": false}
        },
        "size": {"value": 5, "random": true, "anim": {"enable": true, "speed": 5, "size_min": 0, "sync": false}},
        "line_linked": {"enable": false, "distance": 500, "color": "#ffffff", "opacity": 0.4, "width": 2},
        "move": {
            "enable": true,
            "speed": 1,
            "direction": "top",
            "random": true,
            "straight": false,
            "out_mode": "out",
            "bounce": false,
            "attract": {"enable": false, "rotateX": 600, "rotateY": 1200}
        }
    },
    "interactivity": {
        "detect_on": "canvas",
        "events": {
            "onhover": {"enable": false, "mode": "bubble"},
            "onclick": {"enable": false, "mode": "repulse"},
            "resize": true
        },
        "modes": {
            "grab": {"distance": 400, "line_linked": {"opacity": 0.5}},
            "bubble": {"distance": 400, "size": 4, "duration": 0.3, "opacity": 1, "speed": 3},
            "repulse": {"distance": 200, "duration": 0.4},
            "push": {"particles_nb": 4},
            "remove": {"particles_nb": 2}
        }
    },
    "retina_detect": true
});

document.addEventListener("DOMContentLoaded", function () {
    var canvas = document.getElementById("particles-js");
    if (canvas.length) {
        tsParticles.load("tsparticles", {preset: "stars"});
    }
});

var DiscordOnline = (function () {
    var $onlineText = $('[data-toggle="discordonline"]');

    // Init
    function init($onlineText) {
        var $discordID = $onlineText.attr("data-discord-id");
        var $ajaxURL = 'https://discord.com/api/guilds/' + $discordID + '/widget.json';

        $.ajax({
            url: $ajaxURL,
            dataType: "json",
            success: function (data) {
                $onlineText.text(data["presence_count"] + ' ' + lang.users_online);
            },
        });
    }

    if ($onlineText.length) {
        $onlineText.each(function () {
            init($(this));
        });
    }
})();