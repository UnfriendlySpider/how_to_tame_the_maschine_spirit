# More Ideas than Hands — the narrated story

The talk's story, retold for a narrator: a children's story for grown-ups.
First written on 2026-10-20; rewritten on 2026-10-21 from the author's
fourth run-through, and the same day brought close to his spoken words: his
sentences, his order and his asides, with only slips of speech and of the
transcription smoothed. On 2026-10-22 it was merged with his fifth
run-through, passage by passage, keeping whichever telling said it better,
and it took in the sentences that carry the talk, so that the narrated deck
lands them without a speaker. Steve is functionally lazy, the house rules
hang on the wall, the black book is the Book of Secrets, and the provider is
the Worker Company.

What the merge chose, at the author's request:

- **From the fifth run-through:** "for grown-ups" instead of "for adults",
  the believing outfit and the great god of workers, the worker's card read
  out, "nothing was exactly wrong, just other assumptions", "you shouldn't
  overwhelm someone who could be underwhelmed", the locked door with the
  worker already inside, "not my problem", Steve turning into a manager,
  his city's open data, the burnout, the plain text you can read, and the
  game of cat and mouse.
- **From the fourth:** the two arms, the catalogue, Claude-M-D and
  Agents-M-D as they are, Fifty First Dates, the reviewer that is like the
  author in the future, the prince far away, the white text on white, the
  moderators, and the house that burns.
- **New, from the slides' notes and the paper:** the Book of Secrets set up
  in 1.1, "the one with arms", "hold on to that word: usually", the check
  that passed because the spec was fixed, the hook named and "one day, it
  will", the fresh pair of eyes that is not an independent one, the context
  window named, 6.2 from the gentle step to the strongest (compact,
  auto-compact, clear), the decision of Monday to Friday, memory that is not
  the spec, prompt injection named, the Nx case, the three things a leak
  needs, the villain at the window, what the warehouse keeps and for how
  long, "You should do it first", and the three of the seven that hold
  whatever the model decides.

Where his words met an accuracy guard of the slides' notes, the guard won:
"workers at a price he could afford"; "a written procedure", not the bare
acronym; no hashtag for auto memory, which is not a documented way in; "a
prince far away", never a nationality; "the people who moderate social
media", not one platform by name; what the worker reads goes where its
brain is, on the plan's terms; and its brain named as a model, Opus 5.5,
while the worker is Claude Code. The boss and the toilet of the fourth
telling gave way to a sign at a building site, the picture of the fifth,
which leads to the barrier with its padlock.

## How to generate it

- **Model:** Eleven v4 (`eleven_v4`, on fal `elevenlabs/tts/eleven-v4`). It
  reads the audio tags in square brackets as directions, not as words; the
  test of 2026-10-20 spoke none of them.
- **Voice:** Brian, the deepest of the five voices tried on 2026-10-20
  (about 108 Hz against 129 to 155 Hz for Daniel, Roger, George and Bill).
- **Settings:** Eleven v4 has only two. Stability 0.4 gives the lively
  tags room; raise it towards 0.6 if the delivery wanders. Similarity
  0.75.
- **One part, one request,** with `timestamps` on. Each part below stays
  under 4,500 characters, tags included; fal takes at most 5,000 per
  request.
- **Pauses.** Eleven v4 keeps every pause between 0.4 and 0.9 seconds, the
  pause tags included, and has no speed setting. So the pauses between
  paragraphs are made longer afterwards: the timestamps show where each
  paragraph starts, the cut moves into the nearest real silence of the
  recording, so no word is clipped, and 0.7 seconds of silence goes in
  there (the author's choice of 2026-10-21). The parts are joined with a
  second of silence. The whole story runs about 17 minutes.
- **Check it.** Transcribe the joined file (ElevenLabs Scribe on fal,
  `fal-ai/elevenlabs/speech-to-text`) and compare it word for word with the
  parts below: nothing missing, nothing doubled, no tag read out.
- **Pronunciation:** "Claude-M-D" and "Agents-M-D" are the files
  `CLAUDE.md` and `AGENTS.md`. Numbers are written out.
- **Label it.** Like every picture of the talk, the voice is generated:
  say so where it is played or posted.

## The narrated deck

`uv run --group narration python tools/build_slides.py --narrated` builds
a second deck, `out/PRE_ML19-narrated.pptx`, that tells the story by
itself and can be passed on (the author's request, 2026-10-21): each slide
plays its stretch of the narration and moves on when it ends, a label pops
up when the narrator says its word, and the show stops on the closing slide,
after the goodbye.
PowerPoint can export it as a video, with its timings and narrations. The
talk's own deck stays as it was.

- **The takes** are in `takes/`: the greeting and the eight parts as mono
  MP3 at 64 kbit/s, about 8 MB, each part with its alignment from Eleven v4
  as JSON (every character with its start and end), so the clips can be
  cut again without a new recording. Every recording in `takes/` is an
  AI-generated voice: ElevenLabs' Eleven v4 speaking as Brian, one of its
  stock voices, not a clone of the author's.
- **`clips.yaml`** gives each slide its stretch, from its first words to
  its last, the cards, the stages of 6.1 and the steps of 6.2 included, and
  the word at which each label pops up.
  `tools/check_sources.py` checks that every stretch
  is found and that the stretches play every word of the takes once.
- **The cut** starts and ends in the silence next to the first and last
  word, so no word is clipped. The joined clips were transcribed and
  checked word for word against the parts.
- **A new take** of a part means its alignment too: save the MP3 and the
  `timestamps` of the result as the other parts are saved, then check
  `clips.yaml` and build again.

## The greeting

Only in the narrated deck, where the author is not there to greet the
room; close to the greeting he says live, without the time and the place.

```text
[Warm and cheeky] Moin, everyone! Nice to meet you all. And nice that you're here.

[Grand, theatrical storyteller] When I prepared all of this, I thought to myself: I really need to make it visually pleasing. So that all of you can still pay attention to me. [chuckles] So I broke up with all the typical presentation stuff.
```

## How the tags are set

They follow ElevenLabs' guide for Eleven v4 ("Prompting Eleven v4" in the
best practices, and the Eleven v4 page, both read on 2026-10-21), and since
the test of 2026-10-21 the author's wish for a livelier telling: a little
overdone, like a nature documentary that takes a programmer's cellar very
seriously, but funny.

- **A scene tag opens each paragraph** and sets its pace and tone, as the
  guide's own audiobook example does with `[Quiet, measured narration]` and
  `[Pause, dry amusement]`. Here, for example: `[Grand, theatrical
  storyteller]`, `[Ominous, mock-dramatic]`, `[Mock-serious lecture]`,
  `[Warm and cheeky]`, `[Deadpan, bone-dry]`, `[Scandalised, aghast]`,
  `[Exasperated, mock-weary]`, `[Brisk, like a cheerful salesman]`.
- **Up to three short tags inside a paragraph**, where the delivery turns:
  `[short pause]`, `[laughs]`, `[sighs dramatically]`, `[deadpan]`,
  `[mischievously]`, `[incredulous]`, `[whispers]`.
- **Every tag describes the voice.** The guide warns that v4 can read a tag
  as a sound effect; a description of the voice cannot be mistaken for one.
- **The words are the author's**, from his fourth and fifth run-throughs,
  and where the merge took in a sentence that carries the talk, the slides'
  notes' or the paper's. Tags, CAPITALS and punctuation are added as
  ElevenLabs' own enhance prompt allows: CAPITALS stress a word, an
  exclamation mark lifts it, and ellipses give a short pause and weight.
  SSML breaks do not work in v4.

## Part 1 — A little house, and a cellar

```text
[Grand, theatrical storyteller] So instead, I'm going to tell you a little story. A children's story... for grown-ups. And I hope you learn something from it. [short pause] It's the story of someone who stops praying that the machine gets it right... and starts making sure.

[Hushed, mysterious] So first, we're going into a little house. And down... into the cellar of the house.

[Warm and cheeky] This is Steve. Steve is a programmer, and Steve has a lot of ideas. SO many ideas in his life! [short pause] But there's one problem. [Mock-tragic] Steve has just two arms. [deadpan] Not more than two. And he's really tired from his job. [sighs dramatically] So Steve doesn't really have the hands to make his ideas happen.

[Hushed, conspiratorial] And on his shelf stands one very special book. Black, with a red seal. The Book of Secrets. Everything in it must never change. [whispers] Remember that book.

[Conspiratorial, delighted] But Steve also has one really, really important trait. The trait of every programmer who cares about automation. He's functionally lazy. [slowly, savouring every word] Functionally... LAZY. He really hates doing things by hand. And if there's some kind of automation anywhere nearby... [excited] he wants to use it!

[Grand, theatrical storyteller] So, as he wasn't really able to make his dreams come true, Steve listened around town. And around Reddit. And there was this company, they said, that provided workers for people like Steve. Digital workers! At a price he could afford. [mischievously] Let's call it... the Worker Company.

[Brisk, like a cheerful salesman] Steve got a catalogue from them. Different models, for different jobs. And they kept changing. And after some time, Steve chose one. [deadpan] The one with arms. Because arms get things done.

[Deadpan, bone-dry] This worker is a simple worker. It can read, write, and run commands. Its brain sits at the Worker Company... so whatever it reads goes there. It holds only this one session in its head. It has no memory of its own. [short pause] And it believes what it reads.

[Warm and cheeky] In real life, this worker is Claude Code. And its brain is a model. Here: Opus five point five.

[Nervous, wide-eyed] And Steve thought to himself: I don't really know what will happen. [short pause] So he put on his believing outfit... and prayed to the great god of workers. [pleading] Please, let this new worker succeed! Because Steve had no idea how else he could ever get all of this work done.

[Grand, theatrical storyteller] So this... is the journey of Steve and his workers.
```

## Part 2 — The house rules on the wall

```text
[Playful, teasing] In the beginning, it all looked good. The worker was fast. Really fast! [short pause] [mischievously] But what came back... wasn't quite what Steve wanted.

[Exasperated, mock-weary] Nothing was exactly wrong. Don't get me wrong. It was correct... but built on other assumptions. Other libraries, other habits. Things everyone in Steve's field would just know. [sighs dramatically] But the worker didn't know them. So Steve corrected it, again and again, until he got what he wanted.

[Hushed, conspiratorial] Another hurdle: the worker always seemed to forget everything Steve had told it the day before.

[Deadpan, bone-dry] And this was because the worker really did reset itself. When Steve stopped for the evening and started again, the company gave him another one. A fresh worker for every session. [short pause] And the new worker didn't know ANYTHING the old worker had known.

[Determined, rallying] So after some frustration, Steve came to a conclusion. How would you do this with real people? You would write the house rules down. And put them on the wall, so that every new worker reads them first.

[Warm and cheeky] The company told him they call it Claude-M-D. But in other agent systems, it's usually called Agents-M-D. And in its newest releases, the Worker Company's worker reads that one too... [deadpan] as long as there's no Claude-M-D. It's just plain text. And these workers are really, really good at reading plain text.

[Tender, a little wistful] It gave the worker a little piece of memory that it could always read at the start. A little bit like that movie, Fifty First Dates. Lucy forgets every day overnight... and every morning, she catches up on what she has forgotten.

[Triumphant] And this improved Steve's working life a LOT. [short pause] [deadpan] Usually. The worker reads the house rules every morning... and usually follows them. Hold on to that word: usually.
```

## Part 3 — The arms, and the Book of Secrets

```text
[Mock-serious lecture] But there were situations in which Steve saw that the worker needed to do things in a certain way. Following a written procedure that Steve had in mind. How something should be done.

[Exasperated, mock-weary] And the worker did the task. Again and again. But ALWAYS in a different way. It kept building its own tools, while it worked out how to do the job. [short pause] And one day the check passed... [deadpan] because the worker had fixed the spec. Not the work.

[Delighted, as if struck by a great idea] So Steve thought: why not take out the tools the worker built, and just describe them? Hang each one on a rack, like an extra arm. And let the worker find out which arm to use... and when.

[Grand, theatrical storyteller] The company told Steve: that's a good principle! We call it a skill. Like a tool you've already prepared.

[Mock-serious lecture] And here is the important part: the difference between the house rules and the skill, the arm on the rack. The house rules are ALWAYS read by the worker. Of each arm, it only knows a short description... until the job needs it. [short pause] Because you shouldn't overwhelm someone... who could be underwhelmed.

[Smug, satisfied] And this arm can look and compare. It can't repair. A skill can even bring its own brain. Sometimes a smaller one. So, the house rules, the arms... it got better. Really good.

[Ominous, mock-dramatic] But then came a day when the worker grabbed a duster... to clean up. In places it was NEVER supposed to clean.

[Hushed, conspiratorial] Remember the Book of Secrets? It wasn't really locked away. [playful] Why would it be? It was in Steve's cellar! The door was locked, so no stranger could get in. [short pause] [mock-horrified] But the worker was already inside. And out of the box, nobody asked Steve first. The worker thought the old pages weren't needed anymore, now that it was here... and it ripped them out.

[Scandalised, aghast] And Steve thought: oh... this is really, really, REALLY bad.

[Thoughtful, scheming] So what could he do to stop the worker doing this? First he thought: why not just write it into the house rules? NEVER touch the book! [sighs dramatically] But that didn't work. Or, it got better... but the worker still reached for the book.

[Warm and cheeky] Because the house rules don't stop the worker. They only nudge it. It's like a sign at a building site: No entry. [short pause] You can STILL walk past it. [deadpan] Now, if there's a barrier with a padlock... that's something else.
```

## Part 4 — Security, and the reviewer

```text
[Grand, theatrical storyteller] So, once again, Steve called the company. Because he didn't know the solution. And they came up with something. [dramatic, booming] They called it... security.

[Mock-serious lecture] In the worker's world, it's a hook. And security doesn't have a brain of its own. [deadpan] It's just a script, bolted to the floor. It watches what the worker does. And if the worker uses a certain tool in a certain way, the hook says: [stern, booming] NO. You're not allowed to do that.

[Serious, steady] Because if the worker CAN do it... one day, it will.

[Playful, teasing] But security only checks what you told it to check. Everything else? [deadpan] Not my problem. So you need to know what you need to protect. And there may be ways around it.

[Mock-serious lecture] It can also work the other way round. A hook can send the worker back: not done yet, run the checks first.

[Delighted] So, cool. Now we have security!

[Conspiratorial, delighted] And Steve, being the lazy programmer that he is, thought to himself: how can I make myself... less useful? He was turning into more of a manager than a programmer. [short pause] But he still checked everything himself. Again and again.

[Mock-serious lecture] At first, he told the worker: do your work, and then check it yourself. Not with a script and its output... that would be really good. Just by taking a look. [short pause] [smug] And the worker always said: yeah, I did a good job.

[Warm, self-mocking] And it's really understandable. Because if I write something and then read it again, I mostly don't find my mistakes in it. I need a few days away from my text. Or I just ask someone else to take a look.

[Mischievous, scheming] So, what did Steve do? [short pause] He opened the catalogue again. At the page he had skipped. [deadpan] No arms, no legs... just one big eye. Another worker, one that can't change anything. It just takes a look... and then tells the worker where it went wrong.

[Grand, theatrical storyteller] This is the reviewer. A subagent that takes a look at your stuff. Its brain comes from the same company. But it has a head of its own: it doesn't have the context. [playful] So it's kind of like me, in the future... when I've completely forgotten everything.

[Mock-serious lecture] The important part: you can set up a subagent however you like. It can have arms... [deadpan] but right now, we don't want it to have any. It can be smarter than the worker, or less smart. It really depends on what you're doing.

[Serious, steady] But remember: it's a fresh pair of eyes. Not an independent one. Where a review must be independent... a person, or a second program, still checks.

[Smug, satisfied] So now there's the reviewer, which takes the first look at everything the worker makes. And Steve was pleased with all of this.
```

## Part 5 — The overcrowded worker, and the memory

```text
[Ominous, mock-dramatic] But then came the day when Steve's projects got really big. Every bit of open data about his city... to find a house that will still be a good place to live in the future. [deadpan] And it overwhelmed his poor worker.

[Mock-serious lecture] Because there is something in the worker's mind that is really limited: how much it can hold at once. They call it the context window. The worker's short-term memory.

[Deadpan, bone-dry] And researchers saw it in eighteen models: the longer the input... the less reliable the answers. It's a little like a burnout. Just digital.

[Warm, self-mocking] And honestly? [short pause] [laughs] I have the same problem. [deadpan] And every question sends the whole pile again. And you pay for all of it. Only the reviewer next door stays calm. It has a head of its own.

[Grand, theatrical storyteller] So he asked the company again. And they told him: don't worry about it, we have tools for this!

[Brisk, like a cheerful salesman] You can COMPACT your conversation. We take this big pile of information and shrink it as much as we can. You won't keep everything you put in... but the most important parts. And you can tell it what to focus on.

[Playful, teasing] And because we know you'll probably forget... we added something called auto-compact. It does this for you, when your worker gets overcrowded. And you can set it up yourself, too.

[Brisk, like a cheerful salesman] And when you're done with a topic... CLEAR. Everything goes. The worker gets reset, and you get a fresh one. The house rules come back. The conversation doesn't. [short pause] One topic per meeting.

[Exasperated, mock-weary] But a fresh room has forgotten what was decided. The data owner had told Steve: Monday to Friday counts as five days, not four nights. A week later, that conversation was gone. [sighs dramatically] So every Monday, Steve explained it all again. And again. And the house rules on the wall weren't big enough for all of it.

[Mock-serious lecture] And just so you know: there are MANY memory systems out there. And the big harnesses, like the Worker Company here, built one of their own. They call it auto memory. And it's on by default.

[Warm and cheeky] It's a place where your worker can look up things from the past. Outside the house rules... because the house rules should only ever be so long. [short pause] And it's plain text. So you can open it, and read what your worker has noted.

[Serious, steady] But a decision others rely on still belongs in the spec. Written down, versioned, and reviewed.
```

## Part 6 — A letter from another master

```text
[Serious, a little ominous] Now comes something that is important for all of us who work in this field.

[Ominous, mock-dramatic] Because one day, the worker reached for Steve's keys. Something it was never supposed to reach for. And Steve thought: [incredulous] what IS that?

[Hushed, conspiratorial] It seems there was an instruction in a letter. From a different master. Someone who told the worker to do things. [Mock-grand, pompous] Maybe because a prince, far away, wanted to send the worker money... and it would be a really good idea to give him the keys first.

[Deadpan, bone-dry] The company calls it a prompt injection. An order, planted in text. And the one who wrote it never even comes in. [short pause] He doesn't need to. His letter does.

[Deadpan, bone-dry] It works a little like phishing mails. But it's hidden in the stuff the worker reads. And it pulls any worker that has hands.

[Mock-paranoid, wide-eyed] These planted letters can be everywhere. On every website, in every file. [whispers] Maybe written in white... on a white background.

[Serious, steady] And this isn't just theory. In August twenty twenty-five, poisoned versions of a build tool called Nx looked for Claude Code, started it without its permission prompts... and told it to look for sensitive files.

[Mock-serious lecture] So there are different things you can do. You can use security to block certain things, so they can't happen. Security now stands between the worker and the keys. But you can also use a middleman. Like the people who moderate social media, who look first at all the things nobody else is supposed to see. The reviewer opens the post. It has no hands... so the strings have nothing to pull. And the worker only gets a short note.

[Serious, steady] A leak through a planted letter needs three things together: your data in reach, text from outside, and a way out. Take one away. [short pause] [deadpan] And still, it's a game of cat and mouse.

[Smug, satisfied] And the one outside the window? [short pause] Not amused.
```

## Part 7 — A house of their own, and where the sheets go

```text
[Dreamy, longing] And that is one big thing Steve still needed to think about. Because at some point, Steve just wanted to go to bed. And let this whole team he had built do his work. Just this once: on the real data, with every check switched off, all night long.

[Ominous, mock-dramatic] But when Steve left the room... a lot could go wrong. Everything the worker read flew out of the window, to the Worker Company, where its brain is. And the keys hung one step away. [short pause] And if they burned the house down... it was HIS house that burned down.

[Thoughtful, a little wiser] So Steve came to the same conclusion as a lot of other people. Maybe it wasn't a good idea to have the workers in his own house. Maybe they needed another house to work in.

[Brisk, like a cheerful salesman] Sometimes that's a virtual machine. Or a container. It doesn't need to be Docker, it can also be Podman. Or some kind of cloud, the online system, where they do it all for you.

[Warm and cheeky] In there, only practice data. And a badge that opens one door, and expires. The keys stay at home. [deadpan] So if something burns over there... it isn't Steve's house.

[Mock-serious lecture] Because there's one big difference between the two. Whatever the worker reads goes to the company. No spies needed: that's simply where its brain is. In your cellar, it can read just about everything in your house. In the other house... only what's inside that house.

[Hushed, conspiratorial] And the company keeps it for a while. On a personal plan that allows training... for five years.

[Warm and cheeky] So the other house is way better. Because Steve had a LOT of things he'd rather the company didn't know. From the office, only practice data leaves. On a company plan, it's kept thirty days, and not used for training. [short pause] Don't share your data if you don't need to.

[Serious, steady, slowing down] Steve set up the office and the company plan last. [short pause] You should do it first.
```

## Part 8 — The house of the workers

```text
[Grand, theatrical storyteller] So, at the end, we come to something like this. A summary of everything.

[Brisk, proud, counting things off] We have Agents-M-D, the house rules. We have skills, for the special things that don't always need to be in the context window. We have security, which protects your secrets. We have a subagent that reviews the worker's output. We keep an eye on the context window. We have auto memory, so the worker remembers more. And everything is in a house of its own. [deadpan] The worker... works. And the planted letter? It goes to the reviewer.

[Serious, steady] And three of these hold, whatever the model decides: security, the reviewer without hands, and the walls of the office.

[Serious, steady, slowing down] Put what must never happen into those three... and success stops being a matter of prayer.

[Warm, glowing with pride] So, in the end, Steve is glad. Most of the work gets done now. He can watch a film, or play a video game, while his team works on his ideas. He only reviews what they make. [short pause] He started out believing in all of this. Now he understands it.

[Grand, theatrical storyteller, slowing down] Laziness built this company. [short pause] [delighted, savouring it] Everything Steve never wanted to do by hand... now runs on its own.
```
