from subprocess import call

minhafala = "Olá mundo, vamos sintetizar voz com python"

call(["espeak", minhafala])