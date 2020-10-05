#!/usr/bin/env python
# -*- coding: utf-8 -*-
from collections import deque

def check_brackets(text, brackets):

	#pairer les brackets      fermant        ouvrant
	paire_bracket_ouvrante = dict(zip(brackets[0::2], brackets[1::2]))
	paire_bracket_fermant = dict(zip(brackets[1::2], brackets[0::2]))
	bucket = deque()

	for lettre in text:
		#parentase ouvrant
		if lettre in paire_bracket_ouvrante:
			bucket.append(lettre)
		elif lettre in paire_bracket_fermant:
			if len(bucket)==0 or bucket.pop() != paire_bracket_fermant[lettre]:
				return False
	if len(bucket) != 0:
		return False
	else:
		return True

	return paire_bracket

def remove_comments(full_text, comment_start, comment_end):
	while True:
		#trouver le prochaine debut de commentaire
		index_debut=full_text.find(comment_start)

		#trouver la prochaine fin de commentaire
		index_fin = full_text.find(comment_end)

		#si aucun des deux trouvers break C bon
		if index_debut==-1 and -1==index_fin:
				return full_text

		#si fermetur est avant ouverture ou trouver un mais pas l'autre
			#return none
		if index_fin < index_debut or (index_fin==-1) != (index_debut==-1):
				return None
		full_text = full_text[:index_debut]+full_text[index_fin+len(comment_end):]


def get_tag_prefix(text, opening_tags, closing_tags):

	for t in zip(opening_tags,closing_tags):
		if text.startswith(t[0]):
			return (t[0],None)
		elif text.startswith(t[1]):
			return (None,t[1])
	return (None,None)


def check_tags(full_text, tag_names, comment_tags):

	text = remove_comments(full_text,*comment_tags)
	if text is None:
		return False

	#genere les balises
	otags = {f"<{tag}>": f"</{tag}>" for tag in tag_names}
	ctags = { k:v for v,k in otags.items()}


	# while True
	# 	#check si c<Est un tag ouvrant
	# 	tag_potentiel = get_tag_prefix(text,otags,ctags)
	# 	if :
	#
	# 	elif:
	#
	# 	else:


	return ctags

if __name__ == "__main__":
	brackets = ("(", ")", "{", "}")
	yeet = "(yeet){yeet}"
	yeeet = "({yeet})"
	yeeeet = "({yeet)}"
	yeeeeet = "(yeet"
	print(check_brackets(yeet, brackets))
	print(check_brackets(yeeet, brackets))
	print(check_brackets(yeeeet, brackets))
	print(check_brackets(yeeeeet, brackets))
	print()

	spam = "Hello, /* OOGAH BOOGAH */world!"
	eggs = "Hello, /* OOGAH BOOGAH world!"
	parrot = "Hello, OOGAH BOOGAH*/ world!"
	print(remove_comments(spam, "/*", "*/"))
	print(remove_comments(eggs, "/*", "*/"))
	print(remove_comments(parrot, "/*", "*/"))
	print()

	otags = ("<head>", "<body>", "<h1>")
	ctags = ("</head>", "</body>", "</h1>")
	print(get_tag_prefix("<body><h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("<h1>Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("Hello!</h1></body>", otags, ctags))
	print(get_tag_prefix("</h1></body>", otags, ctags))
	print(get_tag_prefix("</body>", otags, ctags))
	print()

	spam = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    </title>"
		"  </head>"
		"  <body>"
		"    <h1>Hello, world</h1>"
		"    <!-- Les tags vides sont ignorés -->"
		"    <br>"
		"    <h1/>"
		"  </body>"
		"</html>"
	)
	eggs = (
		"<html>"
		"  <head>"
		"    <title>"
		"      <!-- Ici j'ai écrit qqch -->"
		"      Example"
		"    <!-- Il manque un end tag"
		"    </title>-->"
		"  </head>"
		"</html>"
	)
	parrot = (
		"<html>"
		"  <head>"
		"    <title>"
		"      Commentaire mal formé -->"
		"      Example"
		"    </title>"
		"  </head>"
		"</html>"
	)
	tags = ("html", "head", "title", "body", "h1")
	comment_tags = ("<!--", "-->")
	print(check_tags(spam, tags, comment_tags))
	print(check_tags(eggs, tags, comment_tags))
	print(check_tags(parrot, tags, comment_tags))
	print()

