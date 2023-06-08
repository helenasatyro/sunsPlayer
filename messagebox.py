from tkinter import *
from tkinter import ttk
import fnmatch
import os
from pygame import mixer
from tkinter import messagebox
from tkinter import scrolledtext as st

capitals = {
    'Always Forever.mp3': '''"We can stay alone together" We silently hang out while being miles apart, and im glad to be able to do so. I know forever is a big word, but for as long as we are good for each other, for as long as our friendship lasts, i hope to live it like a little forever, like always being sure that there is someone in the world as bright as you and who has the same idea of quality time and sharing love as i do. Someone who gets what it means to want  silent company like I do. That's why we work so well, maybe.''',
    'Campfire.mp3': '''One day we'll sit around a campfire with Camz, and this song will mean even more. The notes, our noteits, the flowery road memories and everything we've shared, the friendship that is just comfortable and wholesome like smiling and looking at the moon. It reminds me of you. ''',
    'EVERYTHING.mp3': '''This song's lyrics might be a bit grandiose, however there's something, there are small moments where i've been stopped in my tracks by love. By the overwhelming, shining, soft feeling of overwhelming appreciation; and this song is as big as those feelings are, the crescendo of a heart that is just so happy it wants to explode.''',
    'fairy of shampoo.mp3': '''When i see you, i don't feel lonely. Through a square screen, you softly come. This song, and specifically this version of it, has a dreamlike softness, some comfort, some peace, i think they suit you. Also, are you not tiny and do we not interact through screens? I rest my case.''',
    'Friends.mp3': 'No explanation needed <3',
    'Here Comes The Sun.mp3': '''Here comes Thee Sunny McSun! I'd say it's all gonna be alright.''',
    'Nothing.mp3': '''It's funny how we just exist on discord without saying a word, doing our own things, and yet it's so enjoyable. There's nothing like existing with you, nothing like doing whatever it is as long as you're there. I hope one day we get to exist together in person.''',
    'Partilhar.mp3': '''Let's walk the flowery path together <3''',
    'Pode Vir Comigo.mp3': '''You're incredibly responsible, and you seem to have grown up fast. I hope you can put your worries down a bit, let yourself breathe, and if you want, i'll be here. Not unafraid, not with all the solutions, but with as much support as i can give.''',
    'I Love You More.mp3': 'I do <3',
    'Spring Day.mp3': '''I miss you, yet we never met. Could we have met in another dimension? I can't wait to see you again.''',
    'LOVE YA!.mp3': '''I do! And at times my heart plays this song, in all its energy, upon realizing that I do. (whoever wrote the lyrics seemed to have been a little high tho, dont even ask)''',
    'joyful joyful.mp3': 'This song just has your energy, you bring joy everywhere you go.',
    '오키나와 Okinawa.mp3': '''Let's go to the beach, let's notice right there how we're on the same side of the ocean, lets cry happy tears about it, and lets have them dry under a sun that is almost as bright as you.''',
    'Words Of Love.mp3': '''In a way, we're slowly walking towards each other. As time passes we get closer to the day we'll be in the same room, dancing to whatever, drawing with the same paint, watching a movie and sharing popcorn, dancing to whatever loud song skz puts out.''',
    'THANK U.mp3': 'Thank you. Over and over again.',
    'Love Like You.mp3':'''I wish i was half as good as how you treat me to be. I wish i had a heart half as good as yours. You're inspiring, did you know?''',
    'z playlist link.mp3': '''platonic love isn't talked about enough but boy oh boy am i on a mission to make up for it !!!''',
    'Volta.mp3': '''Maybe we met in a previous life, and that's why i miss you like this. Maybe our paths were meant to cross. Our lives are entangled in strange ways, and i hope you find happiness and become the person you dream to be. And in no way do your plans have to include me, i'll just be overjoyed if one day i just hear the news that you're doing great, if one day we get to catch up and then keep living happy lives. But if you let me, i'd love to be a little keychain.. <3'''}
lyrics = {
    'Always Forever.mp3': '''You and me always forever
We could stay alone together
You and me always forever
Say you'll stay never be separate
You know you've got me in your pocket
You know just have to wait around
You know I'll keep you in my locket
Just come here and we can settle down
You and me always forever
We could stay alone together
Hard to say things could be better
Darling don't get away right now
You know you've got me in your pocket
You know just have to wait around
You know I'll keep you in my locket
Just come here and we can settle down
Oh darling it's alarming thing to think of us apart
You know you've got me in your pocket
You know just have to wait around
You know I'll keep you in my locket
Just come here and we could settle down
You and me always forever
We could stay alone together
You and me always forever
We could stay alone together
You and me always forever
We could stay alone together
You and me always forever
We could stay alone together''',
    'Campfire.mp3': '''you and me together we
너와 내가 함께 우리가

Shall we sit around and look at each other?
같이 둘러앉아 서로를 바라볼까

All the memories on the flower road and the weather that resembles you
너를 닮은 날씨와 꽃길 위에 추억들 모두

If you put out a small note and hand it to each other,
적은 쪽지를 앞으로 내서 서로에게 건네주면
It seemed like it was going to be okay
돼 보일 듯 말듯했던

Let's open our hearts more easily in the future
우리 속마음을 앞으로 더 쉽게

you will find out
알아볼 수 있을 거야

You know each other's eyes
서로의 눈빛 이젠 알잖아

I was only shy in front of you
네 앞에서 쑥스러움뿐이던

I'll make eye contact with you
내가 어느 새 너와 눈 맞춰

The moon shines closer today
오늘따라 달도 가깝게 비치는
brightly illuminated the night sky
밤하늘 밝게 비춘

Our song, our laughter
우리의 노랫소리, 우리의 웃음소리

One by one, I see in the embers
하나 둘씩 튀는 불씨 속에 보이는

Our memories shine brighter
우리 추억 더 밝게 빛나고
Even if today passes
오늘이 지나가도

I hope you don't forget this song we made together, oh
함께 만든 이 노래 잊지 않았으면 해, 오

you next to me, me next to you
내 옆에 있던 너, 네 옆에 있던 나

Our campfire that made each other
서로를 만든 우리의 캠프파이어
you to me, i to you
너는 내게, 나는 너에게

What are you so grateful for?
뭐가 그리도 참 고마웠는지?

I can't let go of the hand we held
잡은 손은 못 떼고 마주친 눈가에도 미소만

It's increasing, time goes by fast, my regrets are already there
늘어가니까, 시간은 빨리 가, 아쉬운 마음은 벌써
You're quicker than me
나보다 눈치도 빠르지

Time passes without knowing the speed
속도 모르고 시간은 흘러가지

It wasn't easy, you and I even here
쉽진 않았지 너와 나 여기까지도

On the way we came, we only trusted each other
오는 길 서로만 믿고 왔지

Because the golden time goes by quickly
금쪽같은 시간 금방 흘러가니까

I want to hold you tight because I'm with you
꽉 붙잡아 두고 싶어 너와 함께니까

In my hand, in front of a guitar and a burning flame
내 손엔 통기타와 타오르는 불꽃 앞에

A train of memories that departs from the past
옛 얘기로 출발하는 추억의 기차
brightly illuminated the night sky
밤하늘 밝게 비춘

Our song, our laughter
우리의 노랫소리, 우리의 웃음소리

One by one, I see in the embers
하나 둘씩 튀는 불씨 속에 보이는

Our memories shine brighter
우리 추억 더 밝게 빛나고
Don't forget that we're only running out of time
우리만은 시간에 쫓겨 잊지는 말아요

How precious, how grateful
얼마나 소중한지, 얼마나 고마운지

Even if the moonlight goes out tomorrow morning
내일 아침에 달빛이 꺼져도

our hearts won't go out
우리 맘은 꺼지지 않아요
when it's hard and you're tired
힘들고 너 지칠 때

I'll light you up, smile brightly
그댈 밝혀 줄게요, 환하게 웃어봐요

Let's all sing together so we can be each other's strength
서로의 힘이 될 수 있게 다 같이 불러봐요

Even after this night
이 밤이 지나도
when it's hard and you're tired
힘들고 너 지칠 때

I'll light you up, don't let go of my hand
그댈 밝혀 줄게요, 내 손을 놓지 마요

You next to me, me by your side
내 옆에 있던 널, 네 옆에 있던 나

Our campfire to light up each other
서로를 밝힐 우리의 캠프파이어''',
    'EVERYTHING.mp3': '''you are my everything

My everything

on a rainy day
비가 내리는 날엔

We lie in our room and say nothing
우리 방안에 누워 아무 말이 없고

When we look into our closed eyes, everything is ours
감은 눈을 마주 보면 모든 게 우리거야

Even when you come to me with a slightly shabby face
조금 핼쑥한 얼굴로 날 찾아올 때도

Sometimes when you surprise me with a funny thing
가끔 발칙한 얘기로 날 놀랠킬 때도

you are my everything
넌 내 모든 거야

It's my summer and it's my dream
내 여름이고 내 꿈이야

you are my everything
넌 내 모든 거야

I'll take it as it is
나 있는 그대로 받아줄게요''',
    'fairy of shampoo.mp3': '''Through the square screen
네모난 화면 헤치며

come to me softly
살며시 다가와

planted a silver illusion
은빛의 환상 심어준

she's my own little fairy
그녀는 나만의 작은 요정
like the early morning mist
이른 아침 안개처럼

come to me
내게로 다가와

wavy long hair
너울거리는 긴 머리

Whisper with a gentle smile
부드런 미소로 속삭이네
When I see her, I don't feel lonely
그녀만 보면 외롭지 않아

Even the sad heart disappears far away
슬픈 마음도 멀리 사라져

she's my shampoo fairy
그녀는 나의 샴푸의 요정

i will love you now
이제는 너를 사랑할꺼야
When I see her, I don't feel lonely
그녀만 보면 외롭지 않아

Even the sad heart disappears far away
슬픈 마음도 멀리 사라져

she's my shampoo fairy
그녀는 나의 샴푸의 요정

i will love you now
이제는 너를 사랑할꺼야
she is my star she is my night
그녀는 나의 별 그녀는 나의 밤

she's my dream she's my eyes
그녀는 나의 꿈 그녀는 나의 눈

just look at her
그녀만 보면''',
    'Friends.mp3': '''Seoul was exceptionally shiny!
유난히도 반짝였던 서울!

Another world I see for the first time
처음 보는 또 다른 세상

I met you full of sweat
땀에 잔뜩 밴 채 만난 넌

kid who was weird
뭔가 이상했었던 아이
I'm from the moon, you from the stars
난 달에서, 넌 별에서

Our conversation was like homework
우리 대화는 숙제 같았지

One day best friend, one day nothing
하루는 베프, 하루는 웬수

I just wanna understand
I just wanna understand
Hello my alien
Hello my alien

We are each other's mystery
우린 서로의 mystery

So is it more special?
그래서 더 특별한 걸까
Someday when these shouts stop, stay, hey
언젠가 이 함성 멎을 때 stay, hey

stay with me
내 옆에 함께 있어줘

Stay here forever, hey
영원히 계속 이곳에 stay, hey

like your little pinkie
네 작은 새끼손가락처럼
Than seven summers and cold winters
일곱 번의 여름과 추운 겨울보다

long time
오래

Than the countless promises and memories
수많은 약속과 추억들보다

long time
오래
Remember our uniforms
우리 교복 차림이 기억나

Our memories one by one movie
우리 추억 한 편 한 편 영화

The dumpling case is a comedy movie yeah, yeah
만두 사건은 코미디 영화 yeah, yeah
The stories that filled the school bus
하교 버스를 채운 속 얘기들

Now let's go out for a drive together
이젠 함께 drive를 나가

It's the same, we at that time
한결같애, 그때의 우리들

"Hey Jimin, today"
"Hey 지민, 오늘"
dream catcher in my room
내 방의 드림캐쳐

7 years of history
7년간의 history

So is it more special?
그래서 더 특별한 걸까
Someday when these shouts stop, stay, hey
언젠가 이 함성 멎을 때 stay, hey

stay with me
내 옆에 함께 있어줘

Stay here forever, hey
영원히 계속 이곳에 stay, hey

like your little pinkie
네 작은 새끼손가락처럼
Than seven summers and cold winters
일곱 번의 여름과 추운 겨울보다

long time
오래

Than the countless promises and memories
수많은 약속과 추억들보다

long time
오래
your little finger
네 새끼손가락

like we are still
처럼 우린 여전해

yes i know everything
네 모든 걸 알아

we have to trust each other
서로 믿어야만 돼

do not forget
잊지 마

Rather than the obvious words of thank you
고맙단 그 뻔한 말 보단

You and me
너와 나

I'm really not going to fight tomorrow
내일은 정말 싸우지 않기로 해
Someday when these shouts stop, stay, hey
언젠가 이 함성 멎을 때 stay, hey

You are my soulmate
You are my soulmate

Stay here forever, hey
영원히 계속 이곳에 stay, hey

You are my soulmate
You are my soulmate
Than seven summers and cold winters
일곱 번의 여름과 추운 겨울보다

long time
오래

Than the countless promises and memories
수많은 약속과 추억들보다

long time
오래
Someday when these shouts stop, stay, hey
언젠가 이 함성 멎을 때 stay, hey

You are my soulmate
You are my soulmate

Stay here forever, hey
영원히 계속 이곳에 stay, hey

You are my soulmate
You are my soulmate
Than seven summers and cold winters
일곱 번의 여름과 추운 겨울보다

long time
오래

Than the countless promises and memories
수많은 약속과 추억들보다

long time
오래''',
    'Here Comes The Sun.mp3': '''Here comes the Sun, doo-doo-doo-doo
Here comes the Sun and I say
It's all right
Little darling
It's been a long cold lonely winter
Little darling
It feels like years since it's been here
Here comes the Sun, doo-doo-doo-doo
Here comes the Sun and I say
It's all right
Little darling
The smiles returning to the faces
Little darling
It seems like years since it's been here
Here comes the Sun
Here comes the Sun and I say
It's all right
Sun, Sun, Sun, here it comes
Sun, Sun, Sun, here it comes
Sun, Sun, Sun, here it comes
Sun, Sun, Sun, here it comes
Sun, Sun, Sun, here it comes
Little darling
I feel that ice is slowly melting
Little darling
It seems like years since it's been clear
Here comes the Sun (doo, doo, doo)
Here comes the Sun and I say
It's all right
Here comes the Sun (doo, doo, doo)
Here comes the Sun
It's all right
It's all right''',
    'Nothing.mp3': '''Track suits and red wine
Movies for two
We'll take off our phones
And we'll turn off our shoes
We'll play Nintendo
Though I always lose
'Cause you'll watch the TV
While I'm watching you
There's not many people
I'd honestly say
I don't mind losing to
But there's nothing
Like doing nothing
With you
Dumb conversations
We lose track of time
Have I told you lately
I'm grateful you're mine
We'll watch The Notebook
For the 17th time
I'll say "It's stupid"
Then you'll catch me crying
We're not making out
On a boat in the rain
Or in a house I've painted blue
But there's nothing
Like doing nothing
With you
So shut all the windows
And lock all the doors
We're not looking for no one
Don't need nothing more
You'll bite my lip and
I'll want you more
Until we end up in a heap on the floor
Mmm
You could be dancing on tabletops
Wearing high-heels
Drinking until the world
Spins like a wheel
But tonight your apartment
Had so much appeal
Who needs stars?
We've got a roof
But there's nothing
Like doing nothing
With you
Mmm
No, there's nothing
Like doing nothing
With you''',
    'Partilhar.mp3': '''If need be, I'll take a boat
Se for preciso, eu pego um barco

I'll row for six months like a fish, to see you
Eu remo por seis meses como peixe, pra te ver

They're yet to invent a sea big enough
Tão pra inventar um mar grande o bastante
That scares me and that I give up on you
Que me assuste e que eu desista de você
If need be I'll create some machine
Se for preciso eu crio alguma máquina

Faster than doubt, more sudden than tears
Mais rápida que a dúvida, mais súbita que a lágrima
I travel at full strength and in an instant of longing and pain
Viajo a toda força e num instante de saudade e dor
I'll arrive to say that I came to see you
Eu chego pra dizer que eu vim te ver

I want to share, I want to share
Eu quero partilhar, eu quero partilhar
the good life with you
A vida boa com você

what a great love
Que amor tão grande

It has to be lived at every instant
Tem que ser vivido a todo instante
Every hour I'm away is a waste
A cada hora que eu tô longe é um desperdício
I only have eighty years to go
Eu só tenho oitenta anos pela frente

Please give me a chance to live
Por favor, me dê uma chance de viver

If I have to, I'll rotate the whole Earth
Se for preciso, eu giro a Terra inteira
Until time forgets
Até que o tempo se esqueça
To go forward and goes back millions of years
De ir pra frente e volte atrás milhões de anos
When all continents met
Quando todos continentes se encontravam
So I can walk to you
Pra que eu possa caminhar até você

And I know, woman, one can't live on fish alone
E eu sei, mulher, não se vive só de peixe
One can't go back to the past
Nem se volta no passado
my words are worth little
As minhas palavras valem pouco
And the vows don't tell you anything
E as juras não te dizem nada

But if there is anyone who can
Mas se existe alguém que pode
Rescue your faith in the world, there is us
Resgatar sua fé no mundo, existe nós

I also lost my way
Também perdi o meu rumo
Even my singing went silent
Até o meu canto ficou mudo

And I suspect that this world is no longer all that
E eu desconfio que esse mundo já não seja tudo aquilo
But it doesn't matter, we invent our life
Mas não importa, a gente inventa a nossa vida
And life is good with you
E a vida é boa com você

I want to share, I want to share
Eu quero partilhar, eu quero partilhar
the good life with you
A vida boa com você

All that remains is here
Tudo que ficou tá aqui''',
    'Pode Vir Comigo.mp3': '''Stop crying, I make you understand
Pare de chorar, te faço entender

That it's better for two if it's us
Que é melhor a dois se formos nós

In any rhythm, in any sea
Em qualquer embalo, em qualquer mar

In any rhythm, at any price
Em qualquer embalo, a qualquer preço

For us
Por nós dois
Stop thinking about what might happen
Pare de pensar no que pode acontecer

Nightmares or out of us
Pesadelos ou pra fora de nós

And any other fear of dreaming
E qualquer outro medo de sonhar

Out of the plot or our home
Pra fora do enredo ou nosso lar

not between us
Não entre nós

Oh, it's not that I'm fearless
Ah, não que eu seja sem medo
But still I'm not afraid
Mas mesmo assim não temo

You can come with me, you can come with me
Pode vir comigo, pode vir comigo

Stop talking, leave everything to its own time
Pare de falar, deixe tudo ao seu tempo

And listen to this song that speaks of us
E ouça essa canção que fala de nós

We don't have a mistake, not a single one
Não temos um erro, um sequer

Because we are perfect
Que nós somos perfeitos

From heart to toes
Desde os pés ao coração

Not that I'm fearless
Não que eu seja sem medo

But still I'm not afraid
Mas mesmo assim não temo

You can come with me, you can come with me
Pode vir comigo, pode vir comigo''',
    'I Love You More.mp3': '''You know that old cliche advice about relationships?
“Let the other person win all the arguments, and
Even when you’re right just bite your tongue”
Well I just can’t let you win this one
I love you more
I love you more
I love you more
I love you more
Baby there’s no question, no competition
I love you more''',
    'Spring Day.mp3': '''보고싶다
I miss you

이렇게 말하니까 더 보고싶다
Saying it like this makes me miss you more

너희 사진을 보고있어도 보고싶다
I miss you even though I’m looking at your photo

너무 야속한 시간
The time is so cruel

나는 우리가 밉다
I hate us

이젠 얼굴 한 번 보는 것도 힘들어진 우리가
Seeing each other for once is now so hard between us

여긴 온통 겨울 뿐이야
It’s all winter here

8월에도 겨울이 와
It’s even winter in August

마음은 시간을 달려가네
My heart is running on the time

홀로 남은 설국열차
Alone on the Snowpiercer

니 손 잡고 지구 반대편까지 가
I want to hold your hand and go to the other side of the earth

겨울을 끝내고파
I want to end this winter

그리움들이 얼마나 눈처럼 내려야
How much longing should we see snowing down

그 봄날이 올까 Friend
For the spring day to come Friend

허공을 떠도는 작은 먼지처럼 작은 먼지처럼
Like a tiny dust (2x) floating in the air

날리는 눈이 나라면 조금 더 빨리 네게 닿을 수 있을 텐데
If only I was the snow in the air, I would get to you a little faster

눈꽃이 떨어져요
Snowflakes fall down

또 조금씩 멀어져요
And they get away little by little

보고 싶다 보고 싶다
I miss you, I miss you

얼마나 기다려야
How long do I have to wait

또 몇 밤을 더 새워야
And how many sleepless night do I have to spend

널 보게 될까  만나게 될까
To see you, to meet you

추운 겨울 끝을 지나
Passing by the edge of the cold winter

다시 봄날이 올 때까지
Until the spring day comes again

꽃 피울 때까지
Until the flower blossoms

그곳에 좀 더 머물러줘 머물러줘
Please stay, please stay there a little longer

니가 변한 건지 아니면 내가 변한 건지
Is it you who have changed or is it me

이 순간 흐르는 시간조차 미워
I hate this moment where the time is flowing

우리가 변한 거지 뭐 모두가 그런 거지 뭐
We have changed but you know, so has everyone

그래 밉다 니가
Yes, I hate you

넌 떠났지만
You left me

단 하루도 너를 잊은 적이 없었지 난
But I never stopped thinking about you, not even a day

솔직히 보고 싶은데 이만 너를 지울게
Honestly, I miss you but I’ll erase you

그게 널 원망하기보단 덜 아프니까
Because it hurts less than to resent you

시린 널 불어내본다 연기처럼 하얀 연기처럼
I try to exhale you in pain like smoke, like white smoke

말로는 지운다 해도 사실 난 아직 널 보내지 못하는데
I say that I’ll erase you but I really can’t let you go yet

[Back to (*)]

You know it all
You're my best friend

아침은 다시 올 거야
The morning will come again

어떤 어둠도 어떤 계절도 영원할 순 없으니까
Because no darkness and no season that can last forever

벚꽃이 피나봐요
Maybe the cherry flower has blossomed

이 겨울도 끝이 나요
And this winter has ended

보고 싶다 보고 싶다
I miss you, I miss you

조금만 기다리면
If you wait a little bit more

며칠 밤만 더 새우면
If you spend a few more sleepless nights

만나러 갈게 데리러 갈게
I’ll be there to see you, I’ll come for you ''',
    'LOVE YA!.mp3': '''Don't be afraid yeah, I will stay
Kick our blanket, make it balloon
Hiding inside
I'll blow all of my love to your lips
Love this quiet moment
"Who would you save
If your best mate and
Me are drowning?"
"I'll save my friend
'Cause you're like a monk seal"
And you asked
"I love you, how much
Can you love me?"
Mm just without
A thousand words
And then I will say
I love ya
I love ya
I love ya
I love ya
Don't be afraid yeah, I will stay
Hide your little spot
With my ring finger
Let's put a name
On each of your every single hairs
Love this quiet moment
"Who would you save
If your best mate
And me are drowning?"
"I'll save my friend
'Cause you're like a monk seal"
You're like me
And I'm like you
What you're thinking right now
It's always the same as me
That's why I'm so in love
I love ya
I love ya
I love ya
I love ya
Na na na na na, na na
Na na na na na, na na
Na na na na na, na na
Na na na na na, na na
I love ya
I love ya
I love ya
I love ya
I love ya
I love ya
I love ya
I love ya''',
    'joyful joyful.mp3': '''Today too, this morning without worries
오늘도 염치없는 이 아침은

Raise me up as if nothing happened
아무 일 없었다는 듯 날 약 올려

A curtain that was cast over and over again
한바탕 욕을 퍼붓고 또 드리운 장막
The stretch that I stretched out like a purple one
보란 듯 펴 보았던 기지개는

When the evening comes, I'm just shy
저녁이 오니 그저 부끄러울 뿐

The curtain that has been withdrawn again and again as if it was picked up
주워 담듯 움츠리고 또 드리운 장막

I'd rather have an eternal dawn
차라리 영원한 새벽을
My prayer will come to mind even tomorrow
나의 기도 내일도 아무렇지 않게 떠오를

Give me strength to laugh at hope
희망 비웃을 힘을 주소서

When I walk along the place where the sun goes down
해가 지는 곳 따라 걷다 보면

that's my joy
그게 내 기쁨이어라
If you pour out the words you endured
참았던 말들을 쏟아 내면은

It must be majestic and noisy
장엄하고 시끄러울 게 뻔해

It's just a spectacle, I'm silent again
구경거리만 될 뿐이야, 난 또다시 침묵

I'd rather have an eternal dawn
차라리 영원한 새벽을
My prayer will come to mind even tomorrow
나의 기도 내일도 아무렇지 않게 떠오를

Give me strength to laugh at hope
희망 비웃을 힘을 주소서

When I walk along the place where the sun goes down
해가 지는 곳 따라 걷다 보면

that's my joy
그게 내 기쁨이어라
Pray that tomorrow will come to mind
기도 내일도 아무렇지 않게 떠오를

Give me strength to laugh at hope
희망 비웃을 힘을 주소서

When I walk along the place where the sun goes down
해가 지는 곳 따라 걷다 보면

that's my joy
그게 내 기쁨이어라''',
    '오키나와 Okinawa.mp3': '''I want to stay by the sea
Watching turn into red
Sat down with the people
Listen through this song
Moon is slowly rising
I see the trees are moving
Sky is brighten through the moon

Look at those trees
Look how they move by the breeze
Look at those stars
Look how they shine through the night''',
    'Words Of Love.mp3': '''The night comes quietly
It talks to me softly
Let's whisper the words of love

The city colored faintly, as the round moon rises
The winter breeze outside the swaying window

Opening the curtain a little and looking out by myself
Around this time
I'm sure you're heading to this room
From somewhere under this sky

Hugging your thin shoulders
I'll talk to you softly
Let's whisper the words of love

I want to keep dancing all night in this spinning world with my girl
The orange light that dyes the room, gently wrapping that girl and me

I would chase the rolling stars in the monochrome night sky
Until that girl comes to this room''',
    'THANK U.mp3': '''These days, sometimes I think
요즘 들어 가끔 난 그런 생각을 해

Maybe I lived pretty well and the proof is you
어쩌면 난 꽤나 잘 살았고 그 증거는 너인 듯해

Although we are aiming at each other,
막상 티격태격 서로를 향해 겨누지만

I was full without knowing how to thank you.
고마운 줄 모르고 배부른 거지 뭐
These words are unfamiliar to me, even if I say every word
이런 말도 낯간지러워 구구절절해도

You know, my truth is yes
알잖아 내 진심은 그래
I have something to say
할 말이 있어

the words i wanted to say
내가 하고 싶었던 그 말

I stayed up all night thinking about it
매일 밤을 지새워 고민했어

thinking of you
널 생각하면

I'm sorry, it was difficult
미안한 게 많아 어렵던

I want to say that now
그 말 이제 하고파
thank you
고마워

(Thank you for being on my side)

so i can walk with you
너와 함께 걸어갈 수 있어서

(Thank you for being on my side)

In a difficult world, we can lean on each other
힘든 세상 서로 기댈 수 있어서
Even if a typhoon hits
태풍이 몰아쳐도

Even if the rain and wind blow
비바람이 불어도
You and me
너와 나

You and me
너와 나

will always be us
언제나 우리일 테니
Yeah even if you don't say anything, good day
Yeah 아무 말 하지 않아도 good day

When everyone, not 1, gathers here
1이 아닌 전부 여기 모였을 때

After falling asleep crazy, at your hum
정신없이 잠든 다음 너의 콧노래에

When I woke up because I couldn’t win, ye
못 이겨서 모두 깼을 때 ye
I can't play comfortably like I used to
예전처럼 편히 놀진 못해

But I pulled out my heart through the cracks, what’s urgent ye ye
But 빈틈 사이로 마음을 꺼내 보니 뭐가 급해 ye ye

Rise and shine every day's a new day, yeah
I have something to say
할 말이 있어

the words i wanted to say
내가 하고 싶었던 그 말

I stayed up all night thinking about it
매일 밤을 지새워 고민했어

thinking of you
널 생각하면

I'm sorry, it was difficult
미안한 게 많아 어렵던

I want to say that now
그 말 이제 하고파
thank you
고마워

(Thank you for being on my side)

so i can walk with you
너와 함께 걸어갈 수 있어서

(Thank you for being on my side)

In a difficult world, we can lean on each other
힘든 세상 서로 기댈 수 있어서
Even if a typhoon hits, wow oh
태풍이 몰아쳐도 wow oh

Even if the rain and wind blow
비바람이 불어도
You and me
너와 나

You and me
너와 나

will always be us
언제나 우리일 테니
The waves stop and the sun rises
파도가 그치고 해가 돋네

I open my eyes and look around me
눈을 떠 내 주위를 바라보네

I feel you are there, I go away
네가 있음을 느껴 난 go away

Let's go together and make a toast to the world
발을 맞춰 세상 속에 건배
There we are in a rough world
거친 세상 그곳에 우리

if we walk together
서로 함께 걷는다면
thank you
고마워

(Thank you for being on my side)

so i can walk with you
너와 함께 걸어갈 수 있어서

(Thank you for being on my side)

In a difficult world, we can lean on each other
힘든 세상 서로 기댈 수 있어서
Even if a typhoon hits, eh
태풍이 몰아쳐도 eh

Even if the rain and wind blow
비바람이 불어도
You and me
너와 나

You and me
너와 나

will always be us
언제나 우리일 테니
you and me you and me
너와 나 너와 나

(Thank you for being on my side)

you and me you and me (you and me)
너와 나 너와 나 (너와 나)

Even if a typhoon hits, eh
태풍이 몰아쳐도 eh

Even if the rain and wind blow
비바람이 불어도
you and me you and me
너와 나 너와 나

It will always be us oh oh oh oh oh oh oh oh oh
언제나 우리일 테니 oh oh oh oh oh oh oh oh oh''',
    'Volta.mp3': '''come, come back
Vem, volta

Cause I've been waiting for you since I was born
Que eu estou te esperando desde que eu nasci

My life for the moment I met you
Minha vida pro momento que eu te conheci

And the love I kept, I kept it for you
E o amor que eu guardava, eu guardei pra você
Go, run
Vai, corre

Go find that which will make you happy
Vai buscar aquilo que vai te fazer feliz

And then come back to my side for us to have some fun
E então volta pro meu lado pra gente curtir

Breezy, just doing what we wanted
Numa boa, só fazendo o que a gente quis
Come back soon, come back soon, come back
Volta logo, volta logo, volta
Come back soon, come back soon, come back
Volta logo, volta logo, volta
Disagree with what I think, I don't care
Discorda do que eu penso, eu não me importo

I just want you
Eu quero só você

So many fears and quirks that I've accumulated
Tantos medos e manias que eu acumulei
When I stay by your side, I tend to forget
Quando eu fico do seu lado, eu costumo esquecer
come, come back
Vem, volta

That I've been waiting for you since I was born
Que eu estou te esperando desde que eu nasci

My life for the moment I met you
Minha vida pro momento que eu te conheci

And the love I kept, I kept it for you
E o amor que eu guardava, eu guardei pra você
And the person I dreamed of, I saw appear
E a pessoa que eu sonhava, eu vi aparecer

And the moments that we had and will have
E os momentos que tivemos e ainda vamos ter

The trips we've taken and will take
As viagens que fizemos e vamos fazer

Or in the hardest times that I comforted you
Ou nos tempos mais difíceis que eu te confortei
If I cried, you arrived, comforted me too
Se eu chorei, você chegou, me confortou também

The beers of the beginning, we got along and turned out well
As cervejas do começo, a gente se deu bem

Jokes with the future and who we're gonna be
Brincadeiras com o futuro e quem nós vamos ser

And the love that we have and will always have
E o amor que a gente tem e sempre vamos ter

And this song after we die
E essa música depois que a gente morrer
Come back soon, come back soon, come back
Volta logo, volta logo, volta
Come back soon, come back soon, come back
Volta logo, volta logo, volta''',
    'Love Like You.mp3': '''If I could begin to be
Half of what you think of me
I could do about anything
I could even learn how to love
When I see the way you act
Wondering when I'm coming back
I could do about anything
I could even learn how to love like you
I always thought I might be bad
Now I'm sure that it's true
'Cause I think you're so good
And I'm nothing like you
Look at you go
I just adore you
I wish that I knew
What makes you think I'm so special
If I could begin to do
Something that does right by you
I would do about anything
I would even learn how to love
When I see the way you look
Shaken by how long it took
I could do about anything
I could even learn how to love like you
Love like you
Love me like you''',
    'z playlist link.mp3': '''https://open.spotify.com/playlist/5FOgt1npp2kZmuPUfrHdyw?si=4308cfadba904b37'''}

if __name__ == '__main__':
    window = Tk()

    window.config(bg="white")
    window.resizable(False, False)
    window_height = 250
    window_width = 270
    icon = PhotoImage(file="icon.png")
    window.iconphoto(True, icon)
    window.title("From Dow (｡•̀ᴗ-)✧")
    style = ttk.Style(window)
    curf = 1
    mixer.init()
    

prev_img = PhotoImage(file="prev_img.png")
pause_img = PhotoImage(file="pause_img.png")
stop_img = PhotoImage(file="stop_img.png")
play_img = PhotoImage(file="play_img.png")
next_img = PhotoImage(file="next_img.png")


def select():
    label.config(text=listbox.get("anchor"))
    print(os.path.join(rootpath, listbox.get("anchor")))
    mixer.music.load(os.path.join(rootpath, listbox.get("anchor")))
    print(os.path.join(rootpath, listbox.get("anchor")))
    mixer.music.play()


def stop():
    mixer.music.stop()
    listbox.select_clear("active")


def play_next():
    try:
        next_song = listbox.curselection()
        next_song = next_song[0] + 1
        next_song_name = listbox.get(next_song)
        label.config(text=next_song_name)
        mixer.music.load(os.path.join(rootpath, next_song_name))
        mixer.music.play()
        listbox.select_clear(0, "end")
        listbox.activate(next_song)
        listbox.select_set(next_song)
    except Exception:
        pass
        label.config(text="No song selected")


def play_prev():
    try:
        next_song = listbox.curselection()
        next_song = next_song[0] - 1
        next_song_name = listbox.get(next_song)
        label.config(text=next_song_name)
        mixer.music.load(os.path.join(rootpath, next_song_name))
        mixer.music.play()
        listbox.select_clear(0, "end")
        listbox.activate(next_song)
        listbox.select_set(next_song)
    except Exception:
        pass
        label.config(text="No song selected")


def pause_song():
    if pauseButton["text"] == "pause":
        mixer.music.pause()
        pauseButton["text"] = "play"
    else:
        mixer.music.unpause()
        pauseButton["text"] = "pause"


def next_frame():
    # curf = int(frame.winfo_name())
    global curf
    curf += 1
    # frame.setvar(name=str(curf))

    if curf == 2:
        frame1.destroy()
        listbox.pack(padx=15, pady=1, anchor="n")
        frame2.pack_configure(expand=True, anchor="n")
        top.pack(padx=10, pady=10, anchor="sw", fill="x")
        # sunnybutton2.pack(padx=10, side="right", in_=top,)
        sunnybutton3.pack(padx=10, side="right", in_=top)
    elif curf == 3:
        frame2.pack_configure(expand=False)
        frame3.pack_configure(expand=False)
        sunnybutton2.destroy()
        listbox.config(height=2)
        listbox.pack_configure(in_=frame3)
        top.pack(padx=10, pady=5, anchor="s", fill="x")
        sunnybutton3.pack(pady=10, padx=10, anchor="se", in_=top)


def message():
    messagewt = str(listbox.get("anchor"))
    if not messagewt == "":
        messagew = Toplevel(bg="white")
        messagew.wm_title(string=messagewt)
        print(messagewt)
        notebook = ttk.Notebook(messagew, width=350)
        tab1 = Frame(notebook)
        tab2 = Frame(notebook)  # new frame for tab 2

        notebook.add(tab1, text="<3")
        text = st.ScrolledText(tab1, height=15, pady=10, padx=10, spacing1=1, wrap=WORD)
        text.insert('1.0', chars=capitals[str(messagewt)])
        text['state'] = 'disabled'
        text.pack()
        notebook.add(tab2, text="lyrics")
        lrcs = st.ScrolledText(tab2, height=15, pady=10, padx=10, spacing1=1, wrap=WORD)
        lrcs.insert('1.0', chars=lyrics[str(messagewt)])
        lrcs['state'] = 'disabled'
        lrcs.pack()
        notebook.pack(expand=True, fill="both")
    else:
        messagebox.showinfo(title="error!", message="Please pick a song then click the sun.")


rootpath = os.path.dirname(__file__)
rootpath = os.path.join(rootpath, "sunsplayer")
pattern = "*.mp3"

# style.theme_use('winnative')
# ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
# get the screen dimension
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# find the center point
center_x = int((screen_width / 2 - window_width / 2) - 10)
center_y = int((screen_height / 2 - window_height / 2) - 50)
# set the position of the window to the center of the screen
window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
# FRAME1
frame1 = Frame(window, bg="white", name="1")
frame1.pack_configure(expand=True)
sunny_png = PhotoImage(file="sunny.png")
sunnybutton = Button(frame1, command=next_frame, text="sunny", bg="white", borderwidth=0, image=sunny_png)
sunnybutton.pack(pady=11)
# sunnybutton.pack(anchor="center")
heartlabel = Label(frame1, anchor="center", text="Hi Sun!")
heartlabel.pack()
heartlabel2 = Label(frame1, anchor="center", text="(click the sun)", font=("arial", 7), bg="white", fg="light gray")
heartlabel2.pack(pady=11)

# FRAME 2

frame2 = Frame(window, bg="white", name="2")
listbox = Listbox(window, fg="gray", bg="white", width=100, height=10, selectbackground="light yellow",
                  selectforeground="orange", font=("Courier New", 10, "bold"))
for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listbox.insert("end", filename)

top = Frame(window, bg="white", height=0)
label = Label(top, text="Pick a song!", bg="white", fg="#ffbb54", font=("Courier New", 10, "bold"))
label.pack(anchor="s")

prevButton = Button(window, text='prev', image=prev_img, bg="white", borderwidth=0, command=play_prev)
prevButton.pack(in_=top, side="left")

stopButton = Button(window, text='stop', image=stop_img, bg="white", borderwidth=0, command=stop)
stopButton.pack(in_=top, side="left")

playButton = Button(window, text='play', image=play_img, bg="white", borderwidth=0, command=select)
playButton.pack(in_=top, side="left")

pauseButton = Button(window, text='pause', image=pause_img, bg="white", borderwidth=0, command=pause_song)
pauseButton.pack(in_=top, side="left")

nextButton = Button(window, text='next', image=next_img, bg="white", borderwidth=0, command=play_next)
nextButton.pack(in_=top, side="left")
sunnybutton2 = Button(window, anchor="center", command=next_frame, text="sunny", bg="white", borderwidth=0,
                      image=sunny_png)

# FRAME 3

frame3 = Frame(window, bg="white", name="3")

sunnybutton3 = Button(window, command=message, anchor="center", text="sunny", bg="white", borderwidth=0,
                      image=sunny_png)

window.mainloop()
