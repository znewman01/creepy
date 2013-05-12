/*global window, document, navigator */
'use strict';

window.addEventListener("DOMContentLoaded", function () {
    var canvas = document.getElementById("canvas"),
        ctx = canvas.getContext("2d"),
        video = document.getElementById("video"),
        videoObj = { "video": true },
        errBack = function (error) {
            console.log("Video capture error: ", error.code);
        };

    // Put video listeners into place
    if (navigator.getUserMedia) {
        navigator.getUserMedia(videoObj, function (stream) {
            video.src = stream;
            video.play();
        }, errBack);
    } else if (navigator.webkitGetUserMedia) { // WebKit-prefixed
        navigator.webkitGetUserMedia(videoObj, function (stream) {
            video.src = window.webkitURL.createObjectURL(stream);
            video.play();
        }, errBack);
    }

    document.getElementById("snap").addEventListener("click", function () {
        ctx.drawImage(video, 0, 0, 640, 480);
        var img = canvas.toDataURL("image/png");
    });
}, false);
