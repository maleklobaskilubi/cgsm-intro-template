# :wave: Základy GitHubu 

## 🤓 Prehľad kurzu a vzdelávacie ciele

Cieľom tohto kurzu je poskytnúť ti stručný úvod do GitHubu. Zároveň ti ponúkneme materiály na ďalšie štúdium a niekoľko nápadov, ktoré ti pomôžu začať pracovať na našej platforme. 🚀

## :octocat: Git a GitHub

Git je **distribuovaný systém na správu verzií (Version Control System, VCS)**, čo znamená, že je užitočným nástrojom na jednoduché sledovanie zmien v tvojom kóde, spoluprácu a zdieľanie. Pomocou Git-u môžeš sledovať zmeny, ktoré robíš vo svojom projekte, takže máš vždy záznam o tom, na čom si pracoval, a v prípade potreby sa môžeš jednoducho vrátiť k staršej verzii. 

Uľahčuje aj spoluprácu – skupiny ľudí môžu pracovať na tom istom projekte a zlúčiť svoje zmeny do jedného finálneho zdrojového kódu!

GitHub je spôsob, ako využívať možnosti Git-u online cez jednoduché webové rozhranie. V softvérovom svete a aj mimo neho sa používa na spoluprácu a na uchovávanie histórie projektov.

GitHub je domovom niektorých z najpokročilejších technológií na svete. Či už vizualizuješ údaje alebo vytváraš novú hru, na GitHube nájdeš celú komunitu a množstvo nástrojov, ktoré ťa posunú na ďalší krok. Tento kurz začína základmi GitHubu, ale k ďalším možnostiam sa dostaneme neskôr.

## :octocat: Pochopenie GitHub flow 

GitHub flow je jednoduchý pracovný postup, ktorý ti umožňuje ľahko experimentovať a spolupracovať na projektoch bez rizika, že prídeš o svoju predchádzajúcu prácu.

### Repozitáre

Repozitár je miesto, kde prebieha práca na tvojom projekte – môžeš si ho predstaviť ako priečinok s projektom. Obsahuje všetky súbory tvojho projektu a históriu ich zmien. V repozitári môžeš pracovať sám alebo môžeš pozvať ďalších ľudí, aby s tebou na súboroch spolupracovali.

### Klonovanie 

Keď je repozitár vytvorený na GitHube, je uložený vzdialene v ☁️. Repozitár si môžeš naklonovať, čím vytvoríš lokálnu kópiu vo svojom počítači, a potom používať Git na synchronizáciu týchto dvoch verzií. Takto je jednoduchšie opravovať problémy, pridávať alebo odstraňovať súbory a odosielať väčšie zmeny (commity). Môžeš tiež používať ľubovoľný editovací nástroj namiesto webového rozhrania GitHubu.

Klonovanie repozitára stiahne aj všetky údaje, ktoré GitHub o repozitári má v danom čase, vrátane všetkých verzií každého súboru a priečinka projektu! To môže byť užitočné, ak experimentuješ s projektom a potom zistíš, že sa ti predchádzajúca verzia páčila viac.  
Ak sa chceš o klonovaní dozvedieť viac, prečítaj si [„Cloning a Repository“](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository). 

### Commitovanie a odosielanie (push)

**Commitovanie** a **pushovanie** sú spôsob, ako pridávať zmeny, ktoré si urobil na svojom počítači, do vzdialeného repozitára na GitHube. Tak môžu tvoj učiteľ a/alebo spolužiaci vidieť tvoju najnovšiu prácu, keď si pripravený sa o ňu podeliť. Commit môžeš vytvoriť, keď si urobil zmeny v projekte, ktoré chceš „zacheckpointovať“. K commitu môžeš pridať aj stručnú **commit message** (správu), ktorá pripomenie tebe alebo tvojim spoluhráčom, čo si urobil (napr. „Pridaný README s informáciami o projekte“).

Keď máš commit alebo viac commitov, ktoré chceš pridať do repozitára, môžeš použiť príkaz push a odoslať tieto zmeny do vzdialeného repozitára. Commitovanie a pushovanie môže byť na začiatku nové a nezvyčajné, ale rýchlo si na ne zvykneš 🙂


## 💻 Pojmy z GitHubu, ktoré by si mal poznať 

### Repozitáre 

Repozitáre sme už spomínali – sú to miesta, kde prebieha práca na tvojom projekte, ale poďme sa na ne pozrieť trochu podrobnejšie. Ako budeš GitHub používať viac, budeš mať pravdepodobne veľa repozitárov, čo môže byť spočiatku mätúce. Našťastie ti s orientáciou pomôže tvoj [„GitHub dashboard“](https://docs.github.com/en/github/setting-up-and-managing-your-github-user-account/about-your-personal-dashboard), kde môžeš jednoducho prechádzať svoje repozitáre a vidieť o nich užitočné informácie. Uisti sa, že si prihlásený!

Repozitáre obsahujú aj súbory **README**. Do repozitára môžeš pridať README, aby si ostatným povedal, prečo je tvoj projekt užitočný, čo s ním môžu robiť a ako ho používať. Tento README používame na to, aby sme ti vysvetlili, ako sa učiť Git a GitHub. 😄  
Ak sa chceš o repozitároch dozvedieť viac, prečítaj si [„Creating, Cloning, and Archiving Repositories“](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-repositories) a [„About README's“](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/about-readmes). 

### Vetvy (branches)

Môžeš používať vetvy (branches) na GitHube na oddelenie práce, ktorú zatiaľ nechceš zlúčiť do finálnej verzie projektu. Vetvy ti umožnia vyvíjať nové funkcie, opravovať chyby alebo bezpečne experimentovať s novými nápadmi v oddelenej časti repozitára. 

Zvyčajne si vytvoríš novú vetvu z predvolenej vetvy repozitára – napríklad main. Tým vznikne nová pracovná kópia repozitára, v ktorej môžeš experimentovať. Keď spoluhráč tvoje zmeny skontroluje alebo keď si s nimi spokojný, môžeš ich zlúčiť (merge) do predvolenej vetvy repozitára.  
Ak sa chceš o vetvách dozvedieť viac, prečítaj si [„About Branches“](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-branches).

### Forky

Fork je ďalší spôsob, ako skopírovať repozitár, najčastejšie vtedy, keď chceš prispieť do cudzieho projektu. Vytvorením forku môžeš slobodne experimentovať so zmenami bez toho, aby si ovplyvnil pôvodný projekt, a tento postup je veľmi populárny pri prispievaní do open source projektov!  
Ak sa chceš o forkoch dozvedieť viac, prečítaj si [„Fork a repo“](https://docs.github.com/en/github/getting-started-with-github/fork-a-repo).

### Pull requesty

Pri práci s vetvami môžeš použiť *pull request* na to, aby si ostatným oznámil zmeny, ktoré chceš zaviesť, a požiadal ich o spätnú väzbu. Keď pull request otvoríš, môžeš o navrhovaných zmenách diskutovať so spolupracovníkmi, kontrolovať ich a podľa potreby pridávať ďalšie úpravy. 

Ku pull requestu môžeš pridať konkrétnych ľudí ako *reviewerov*, čím im dáš najavo, že chceš ich názor na svoje zmeny. Keď je pull request pripravený, môže byť zlúčený do hlavnej vetvy (main) tvojho repozitára.  
Ak sa chceš o pull requestoch dozvedieť viac, prečítaj si [„About Pull Requests“](https://docs.github.com/en/github/collaborating-with-issues-and-pull-requests/about-pull-requests). 


### Issues

Issues (problémy/úlohy) sú spôsob, ako sledovať vylepšenia, úlohy alebo chyby vo tvojej práci na GitHube. Sú skvelým nástrojom na evidenciu všetkých úloh, na ktorých chceš v projekte pracovať, a zároveň ostatným ukazujú, čo plánuješ robiť. Issues môžeš použiť aj na to, aby si svojmu obľúbenému open source projektu nahlásil chybu alebo navrhol novú funkciu, ktorá by sa ti páčila.

Pri väčších projektoch môžeš množstvo issues sledovať na projektovej nástenke (*project board*). GitHub Projects ti pomôžu organizovať a prioritizovať tvoju prácu a viac sa o nich môžeš dočítať [v dokumente „About Project boards“](https://docs.github.com/en/github/managing-your-work-on-github/about-project-boards). Projektovú nástenku pravdepodobne nebudeš pre školské zadania potrebovať, ale pri väčších projektoch je to skvelý spôsob, ako organizovať tímovú prácu!

Pull requesty a issues môžeš navzájom prepojiť, aby bolo vidno, že sa na riešení problému pracuje, a aby sa issue po zlúčení pull requestu automaticky uzavrel.  
Ak sa chceš o issues a ich prepájaní s pull requestmi dozvedieť viac, prečítaj si [„About Issues“](https://docs.github.com/en/github/managing-your-work-on-github/about-issues). 

### Tvoj používateľský profil

Tvoja profilová stránka rozpráva ostatným príbeh o tvojej práci – cez repozitáre, o ktoré sa zaujímaš, príspevky, ktoré si urobil, a konverzácie, do ktorých sa zapájaš. Svoj profil môžeš ešte viac prispôsobiť prostredníctvom profilového README, vďaka ktorému svet uvidí, kto si. Profil môžeš využiť aj na to, aby si sa predstavil budúcim zamestnávateľom. 

Ak sa chceš dozvedieť viac o svojom používateľskom profile a o tom, ako pridať alebo aktualizovať profilové README, prečítaj si [„Managing Your Profile README“](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/managing-your-profile-readme). 

### Používanie Markdownu na GitHube 

Možno si si už všimol, že do issues, pull requestov a súborov môžeš pridávať rôzne formátovanie. [„Markdown“](https://guides.github.com/features/mastering-markdown/) je jednoduchý spôsob, ako pomocou pár znakov naformátovať text v issues, pull requestoch a súboroch. Pomáha lepšie organizovať informácie a uľahčuje ich čítanie ostatným. Môžeš vkladať aj gify a obrázky, aby si lepšie vyjadril, čo chceš povedať.  

Ak sa chceš o používaní GitHub verzie Markdownu dozvedieť viac, prečítaj si [„Basic Writing and Formatting Syntax“](https://docs.github.com/en/github/writing-on-github/basic-writing-and-formatting-syntax). 

### Zapájanie sa do komunity na GitHube

Komunita na GitHube je obrovská. Nájdeš v nej rôzne typy používateľov – študentov ako ty, profesionálnych vývojárov, nadšencov pracujúcich na open source projektoch aj ľudí, ktorí sa do sveta softvérového vývoja len púšťajú. S komunitou môžeš interagovať rôznymi spôsobmi, tu sú tri miesta, kde môžeš začať. 

#### Označovanie repozitárov hviezdičkou (starring)

Ak nájdeš repozitár, ktorý ťa zaujíma alebo si ho chceš zapamätať, označ ho hviezdičkou (*star*). Keď repozitár označíš, GitHub to použije ako signál na zobrazovanie lepších odporúčaní na stránke github.com/explore. K svojim označeným repozitárom sa môžeš kedykoľvek vrátiť cez svoj používateľský profil.  
Ak sa chceš o označovaní repozitárov dozvedieť viac, prečítaj si [„Saving Repositories with Stars“](https://docs.github.com/en/github/getting-started-with-github/saving-repositories-with-stars). 

#### Sledovanie používateľov 

Na GitHube môžeš sledovať (follow) iných používateľov, aby si dostával upozornenia na ich aktivitu a objavoval projekty z ich komunít. Keď niekoho sleduješ, jeho verejná aktivita na GitHube sa bude zobrazovať na tvojom dashboarde, takže uvidíš všetko zaujímavé, na čom pracuje.  
Ak sa chceš o sledovaní používateľov dozvedieť viac, prečítaj si [„Following People“](https://docs.github.com/en/github/getting-started-with-github/following-people).

#### Prehliadanie GitHub Explore 

GitHub Explore je skvelé miesto na to, čo napovedá už názov – na objavovanie :smile: Nájdeš tam nové projekty, podujatia a vývojárov, s ktorými sa môžeš spojiť.

Stránku GitHub Explore si môžeš pozrieť na adrese [github.com/explore](https://github.com/explore). Čím viac GitHub používaš, tým viac sa obsah na stránke Explore prispôsobí tvojim záujmom. 


## 📝 Voliteľné ďalšie kroky 

* Otvor pull request a daj svojmu učiteľovi vedieť, že si tento kurz dokončil.  
* V tomto repozitári vytvor nový markdown súbor. Napíš, čo si sa naučil a čo ti ešte nie je jasné! Experimentuj s rôznymi štýlmi!
* Vytvor svoj profilový README. Povedz svetu niečo viac o sebe! Čo sa chceš učiť? Na čom pracuješ? Aký je tvoj obľúbený koníček? Viac o vytváraní profilového README sa dozvieš v dokumente [„Managing Your Profile README“](https://docs.github.com/en/github/setting-up-and-managing-your-github-profile/managing-your-profile-readme).
* Prejdi na svoj používateľský dashboard a vytvor nový repozitár. Experimentuj s jeho funkciami, aby si ich lepšie spoznal. 
* [Daj nám vedieť, čo sa ti na tomto kurze páčilo alebo nepáčilo](https://support.github.com/contact/education). Čo by si chcel vidieť viac? Čo by ti pomohlo na tvojej študijnej ceste? 


## 📚 Zdroje 

* [Krátke video vysvetľujúce, čo je GitHub](https://www.youtube.com/watch?v=w3jLJU7DT5E&feature=youtu.be) 
* [Učebné zdroje o Gite a GitHube](https://docs.github.com/en/github/getting-started-with-github/git-and-github-learning-resources) 
* [Pochopenie GitHub flow](https://guides.github.com/introduction/flow/)
* [Ako používať vetvy na GitHube](https://www.youtube.com/watch?v=H5GJfcp3p4Q&feature=youtu.be)
* [Interaktívne výukové materiály pre Git](https://githubtraining.github.io/training-manual/#/01_getting_ready_for_class)
* [GitHub Learning Lab](https://lab.github.com/)
* [Diskusné fórum komunity Education](https://education.github.community/)
* [GitHub community fórum](https://github.community/)
