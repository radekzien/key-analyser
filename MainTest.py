from pydub import AudioSegment
import os
from AnalyseKey import AnalyseKey

'''
Kept this file in for marking although it has no use in the final product.
Used for evaluating the algorithm.
'''
# ---- AUDIO ARRAYS ----
classical_audio = [
    'test_audio/Classical/Carnaval, Op. 9： No. 1, Préambule (Live in Japan, 2022).mp3',
    'test_audio/Classical/Carnaval, Op. 9： No. 5, Eusebius (Live in Japan, 2022).mp3',
    'test_audio/Classical/Cello Sonata in B-Flat Major, RV 47： I. Preludio.mp3',
    'test_audio/Classical/Debussy： Deux arabesques, L. 66： No. 1 Andante con moto.mp3',
    'test_audio/Classical/Der Nussknacker, Op. 71, Klaviersuite： IV. Schneeflocken-Walzer.mp3',
    'test_audio/Classical/Fantasie No. 1 in E-Flat Major (Transcr. H. Büsser for Cornet & Organ).mp3',
    'test_audio/Classical/First Encounter.mp3',
    'test_audio/Classical/La vergine degli angeli by Eva-Maria Westbroek (La forza del Destino).mp3',
    'test_audio/Classical/Piano Sonata in E Minor, Op. 7： III. Alla menuetto.mp3',
    'test_audio/Classical/YUNDI plays Mozart： Piano Sonata No. 11 in A Major, K. 331 ＂Alla Turca＂： III. Rondo alla Turca.mp3',
    'test_audio/Classical/Beethoven 3.1.mp3',
    'test_audio/Classical/Beethoven 9.1.mp3',
    'test_audio/Classical/Mahler_ Symphony No 2, 1st movement (Valery Gergiev, London Symphony Orchestra).mp3',
    'test_audio/Classical/Mozart 4.1 C Major.mp3',
    'test_audio/Classical/Shostakovich_ Jazz Suite No. 1_ I. Waltz.mp3'
]

classical_keys = [
    "Ab major",
    "F minor",
    "Bb major",
    "E major",
    "D minor",
    "Eb major",
    "G major",
    "F# major/Gb major",
    "E minor/Fb minor",
    "A major",
    "Eb major",
    "D minor",
    "C minor",
    "C major", 
    "G minor"
]

electro_audio = [
    'test_audio/Electro/A.M.R - Smile [Monstercat Release].mp3',
    'test_audio/Electro/Be Free.mp3',
    'test_audio/Electro/Ca7riel - KEYHOLE (instrumental).mp3',
    'test_audio/Electro/DJ Snake, Lauv - A Different Way (Audio).mp3',
    'test_audio/Electro/IKEA STELPAN.mp3',
    'test_audio/Electro/Justice - D.A.N.C.E. - † (Official Audio).mp3',
    'test_audio/Electro/Kavinsky - Nightcall (Official Audio - HD).mp3',
    'test_audio/Electro/Morcheeba - Blood Like Lemonade [HQ ].mp3',
    'test_audio/Electro/Rezz - Sacrificial (Audio) ft. PVRIS.mp3',
    'test_audio/Electro/Teardrop.mp3',
    'test_audio/Electro/Charlotte De Witte - One Mind.mp3',
    'test_audio/Electro/Cops and Robbers - Sammy Virji.mp3',
    'test_audio/Electro/Layton Giordani - Act of God.mp3',
    'test_audio/Electro/Modestep - Give up the Ghost.mp3',
    'test_audio/Electro/Section - LYNY.mp3'
]

electro_keys = [
    "C# major/Db major",
    "Bb minor",
    "C major",
    "Ab ajor",
    "F# major/Gb major",
    "F# major/Gb major",
    "A minor",
    "F major",
    "G major",
    "B minor",
    "C# minor/Db minor",
    "A major",
    "B major",
    "A major",
    "Ab major"
]

hiphop_audio = [
    'test_audio/HipHop/A$AP Rocky - Praise The Lord (Da Shine) (Official Audio) ft. Skepta.mp3',
    'test_audio/HipHop/Burna Boy - Last Last [Audio].mp3',
    'test_audio/HipHop/Dr. Dre - Still D.R.E. (feat. Snoop Dogg).mp3',
    'test_audio/HipHop/Future - Mask Off.mp3',
    'test_audio/HipHop/Gangstas Paradise.mp3',
    'test_audio/HipHop/In A Minute.mp3',
    'test_audio/HipHop/In Da Club.mp3',
    'test_audio/HipHop/Love & War.mp3',
    'test_audio/HipHop/Mac Miller - Cinderella (feat. Ty Dolla $ign).mp3',
    'test_audio/HipHop/One Dance (feat. WizKid & Kyla) - Drake (Official Audio).mp3',
    'test_audio/HipHop/Clipse - So Be It.mp3',
    'test_audio/HipHop/Come n Go - Yeat.mp3',
    'test_audio/HipHop/Gunna - Him All Along.mp3',
    'test_audio/HipHop/NBA Youngboy - Shot Callin.mp3',
    'test_audio/HipHop/Playboi Carti - Like Weezy.mp3'
]

hiphop_keys = [
    "F minor",
    "Eb minor",
    "B major",
    "D major",
    "Ab major",
    "E minor/Fb minor",
    "F# minor/Gb minor",
    "B minor",
    "Ab minor",
    "C# major/Db major",
    "D major",
    "A minor",
    "E minor",
    "Ab major",
    "D major"
]


jazz_audio = [
    'test_audio/Jazz/And Then There Was You.mp3',
    'test_audio/Jazz/Anita Baker - Body And Soul.mp3',
    'test_audio/Jazz/Delarna.mp3',
    'test_audio/Jazz/Es kommt zum Duell.mp3',
    'test_audio/Jazz/Goodbye, Old Girl.mp3',
    'test_audio/Jazz/Nina Simone - I Put A Spell On You (Audio).mp3',
    'test_audio/Jazz/O Tannenbaum.mp3',
    'test_audio/Jazz/Sarah Vaughan - Embraceable You (EmArcy Records 1954).mp3',
    'test_audio/Jazz/This Is A Very Special Day.mp3',
    'test_audio/Jazz/Unforgettable.mp3',
    'test_audio/Jazz/Autumn Leaves - Eddie Higgins.mp3',
    'test_audio/Jazz/Dave Brubeck - Take Five.mp3',
    'test_audio/Jazz/Duke Ellington - Take the A Train.mp3',
    'test_audio/Jazz/Miles Davis - So what.mp3',
    'test_audio/Jazz/Mississippi Goddam - Nina Simone.mp3'
]

jazz_keys = [
    "Bb major",
    "Ab major",
    "D major",
    "F minor",
    "G major",
    "F# minor/Gb minor",
    "Eb major",
    "C major",
    "G minor",
    "F major",
    "G minor",
    "Eb minor",
    "C major",
    "D minor",
    "F major"
]

metal_audio = [
    'test_audio/Metal/Avenged Sevenfold - Hail to the King (Audio).mp3',
    'test_audio/Metal/Bring Me The Horizon - Can You Feel My Heart.mp3',
    'test_audio/Metal/Ghost - Mary On A Cross (Official Audio).mp3',
    'test_audio/Metal/Heaven Nor Hell (Single Version).mp3',
    'test_audio/Metal/Here Without You.mp3',
    'test_audio/Metal/I Put A Spell On You.mp3',
    'test_audio/Metal/Killing in the Name.mp3',
    'test_audio/Metal/Korn - Rotting In Vain (Audio).mp3',
    'test_audio/Metal/System of a Down - Aerials (Remastered 2021).mp3',
    'test_audio/Metal/Walk (2010 Remaster).mp3',
    'test_audio/Metal/Black Sabbath - Paranoid (Official Audio).mp3',
    'test_audio/Metal/Enter Sandman (Remastered).mp3',
    'test_audio/Metal/Iron Maiden - The Trooper.mp3',
    'test_audio/Metal/Slipknot - Duality (LYRICS).mp3',
    'test_audio/Metal/System of a Down - Chop Suey (Remastered 2021).mp3'
]

metal_keys = [
    "Eb minor",
    "E minor/Fb minor",
    "B major",
    "Eb major",
    "Bb minor",
    "B minor",
    "G major",
    "D major",
    "C minor",
    "F# minor/Gb minor",
    "E minor/Fb minor",
    "E minor/Fb minor",
    "E minor/Fb minor",
    "D minor",
    "E minor/Fb minor"
]

pop_audio = [
    'test_audio/Pop/09 Sean Paul - No Lie Ft. Dua Lipa [Official Audio].mp3',
    'test_audio/Pop/Avicii - The Nights.mp3',
    'test_audio/Pop/Charlie Puth - Attention (Audio).mp3',
    'test_audio/Pop/Chris Brown - Under The Influence (Audio).mp3',
    'test_audio/Pop/Ed Sheeran - 2step.mp3',
    'test_audio/Pop/Heat Waves.mp3',
    'test_audio/Pop/Lana Del Rey - Doin Time (Official Audio).mp3',
    'test_audio/Pop/Somebody To You.mp3',
    'test_audio/Pop/The Weeknd - Blinding Lights (Official Audio).mp3',
    'test_audio/Pop/The Weeknd - Take My Breath (Official Audio).mp3',
    'test_audio/Pop/ABBA - Dancing Queen.mp3',
    'test_audio/Pop/Back Street Boys - I want it that way.mp3',
    'test_audio/Pop/I Wanna Dance With Somebody - Whitney Houston.mp3',
    'test_audio/Pop/Madonna - Like a prayer.mp3',
    'test_audio/Pop/Michael Jackson - Billie Jean.mp3'
]

pop_keys = [
    "G major",
    "F# major/Gb major",
    "Eb minor",
    "A minor",
    "E minor/ Fb minor",
    "B major",
    "G minor",
    "Eb major",
    "C# major/Db major",
    "Ab major",
    "A major",
    "A major",
    "A major",
    "D minor",
    "F# minor/Gb minor"
]

# ---- TEST FUNCTION ----
total = 0

def test(audios, keys, printName):
    global total
    print("---", printName, "---")
    local_total = 0

    for i, mp3_path in enumerate(audios):
        print(mp3_path)
        wav_path = mp3_path.replace(".mp3", ".wav")
        if not os.path.exists(wav_path):
            audio = AudioSegment.from_file(mp3_path)
            audio.export(wav_path, format="wav")
        key = AnalyseKey(wav_path)
        print("     Expected:", keys[i])
        print("     Received: ", key)
        if key == keys[i]:
            local_total += 1
            total += 1

    print(f"{local_total}/{len(audios)} {(local_total/len(audios))*100:.2f}%\n")


# ---- RUN TESTS ----
test(classical_audio, classical_keys, "CLASSICAL")
test(jazz_audio, jazz_keys, "JAZZ")
test(electro_audio, electro_keys, "ELECTRONIC")
test(hiphop_audio, hiphop_keys, "HIP-HOP")
test(pop_audio, pop_keys, "POP")
test(metal_audio, metal_keys, "METAL")

print(f"TOTAL ACCURACY: {total} {(total/len(classical_audio+electro_audio+jazz_audio+hiphop_audio+pop_audio+metal_audio))*100:.2f}")
