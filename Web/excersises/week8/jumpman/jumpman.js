const jumpBtn = document.getElementById("jump_btn");
const stopBtn = document.getElementById("stop_btn");

let jumping = false;

jumpBtn.addEventListener("click", async () => {
    jumping = true;
    const animation = document.getElementById("animated_img");

    flow = false;

    while (jumping) {
        img_src = animation.src;
        if (img_src.includes("jump0.gif")) {
            flow = !flow;        
            animation.src = "jump1.gif";
        } else if (img_src.includes("jump1.gif")) {
            if (flow) {
                animation.src = "jump2.gif";
            } else {
                animation.src = "jump0.gif";
            }
        } else if (img_src.includes("jump2.gif")) {
            if (flow) {
                animation.src = "jump3.gif";
            } else {
                animation.src = "jump1.gif";
            }
        } else if (img_src.includes("jump3.gif")) {
            flow = !flow;
            animation.src = "jump2.gif";
        }

        await new Promise(resolve => setTimeout(resolve, 100));
    }
});

stopBtn.addEventListener("click", function(event) {
    jumping = false;
});