/*global window, document, navigator */
'use strict';

(function ($) {
    $(function () {
        var canvas = $("canvas")[0],
            ctx = canvas.getContext("2d"),
            video = $("video")[0],
            videoObj = { "video": true },
            errBack = function (error) {
                console.log("Video capture error: ", error.code);
            };

        function sendImage() {
            ctx.drawImage(video, 0, 0, 640, 480);
            var img = canvas.toDataURL("image/png");
            $.post("/upload", {"image": img}, function (data) {
                $("#face").html('<img src="data:image/png;base64,' + data + '" />');
            });
        }

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
        sendImage();

        $("#snap").click(sendImage);
    });
}(window.jQuery));
