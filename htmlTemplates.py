css = '''
<style>
.egzxvld5 {
    background-image:url("https://www.juncyber.com/wp-content/uploads/2024/04/Untitled-design-1-1.png");
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
}
.euu6i2w0 {
    background-color:white;
}
.css-1aehpvj{
    color:white;
}
.stSpinner{
    background-color:white;
}
.uploadedFile{
    color:white;
}
.e1fqkh3o3 {
    background-color:#072942;
}

 .ex0cdmw0{
    color:white;
}
.ss-1aehpvj {
color:black;
}
.euu6i2w0{
    color:black;
}
.ex0cdmw0:hover{
    scale:2;
}
.e16nr0p31 h3{
    color:white;
    font-size:2em;
}
.e16nr0p34{
    color:white;

}
.css-1offfwp{
    color:black;
    text-align:center;
}
#businessbot {
    color:white;
    font-size:3.5em;

}
#the-pdf-query-engine {
    color:white;
    font-size: 1 em;
}
#by-j-n-cyber  {
    color:white;
    font-size:1em;

}
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 20%;
}
.chat-message .avatar img {
  max-width: 78px;
  max-height: 78px;
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 80%;
  padding: 0 1.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://media.licdn.com/dms/image/C4E0BAQE0UkHmUn_Mww/company-logo_200_200/0/1630653924576/juncyber_logo?e=2147483647&v=beta&t=UO9PR-DnPcqlIKGwi-wu4vaubSqbnjX2WtwC596oDi8" style="max-height: 78px; max-width: 78px; border-radius: 50%; object-fit: cover;">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img src="https://static.vecteezy.com/system/resources/previews/005/005/788/original/user-icon-in-trendy-flat-style-isolated-on-grey-background-user-symbol-for-your-web-site-design-logo-app-ui-illustration-eps10-free-vector.jpg">
    </div>    
    <div class="message">{{MSG}}</div>
</div>
'''
