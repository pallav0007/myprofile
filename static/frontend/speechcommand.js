function speak(string) {
  const u = new SpeechSynthesisUtterance();
  allVoices = speechSynthesis.getVoices();
  u.voice = allVoices.filter(voice => voice.name === "Alex")[0];
  u.text = string;
  u.lang = "en-US";
  u.volume = 1; //0-1 interval
  u.rate = 1;
  u.pitch = 1; //0-2 interval
  speechSynthesis.speak(u);
}
function getresponse(text) {
    let userText = text

    console.log("usertext"+userText+"text");
    let userHtml = '<p  class="userText"><span>' + userText + '</span></p>';
    // $("#final").val("");
    $(".chat-text").append(userHtml);
    // document.getElementById('chat-text').scrollIntoView({block: 'start', behavior: 'smooth'});
    $.get("/chat",{ msg: userText }).done(function(data) {
        var botHtml = '<p  class="botText"><span>' + data + '</span></p>';
        console.log(data)
        $(".chat-text").append(botHtml);
        speak(data)
        // document.getElementById('chat-text').scrollIntoView({block: 'start', behavior: 'smooth'});
});
}
if ("webkitSpeechRecognition" in window) {
  let speechRecognition = new webkitSpeechRecognition();
  let final_transcript = "";
  let text="";

  speechRecognition.continuous = true;
  speechRecognition.interimResults = true;
  speechRecognition.lang = document.querySelector("#select_dialect").value;

  speechRecognition.onstart = () => {
    document.querySelector("#status").style.display = "block";
  };
  speechRecognition.onerror = () => {
    document.querySelector("#status").style.display = "none";
    console.log("Speech Recognition Error");
  };
  speechRecognition.onend = () => {
    document.querySelector("#status").style.display = "none";
    console.log("Speech Recognition Ended");
  };

  speechRecognition.onresult = (event) => {
    let interim_transcript = "";
    final_transcript=""
    for (let i = event.resultIndex; i < event.results.length; ++i) {
      if (event.results[i].isFinal) {
        final_transcript += event.results[i][0].transcript;

      } else {
        interim_transcript += event.results[i][0].transcript;
      }
    }
    document.querySelector("#final").innerHTML = final_transcript;
    document.querySelector("#suggest").innerHTML = interim_transcript;
  };

  document.querySelector("#start").onclick = () => {
    speechRecognition.start();
  };
  document.querySelector("#stop").onclick = () => {
      console.log("pallav answered");
      console.log(text)
      getresponse(final_transcript);
    speechRecognition.stop();
  };
} else {
  console.log("Speech Recognition Not Available");
}