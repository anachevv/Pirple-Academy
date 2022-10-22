//MY FAVOURITE SONG

//This file shows information about my favourite song:
//Song name
//Nationality
//Artists
//Genre
//Year Released
//Duration
//Number of views
//Lyrics

//Created by: Anatoli
package favouritesong;

import java.util.*;

public class FavouriteSong {
    
    @SuppressWarnings("empty-statement")
    public static void main(String[] args) {
        String[] allElements;
        allElements =
                {"Колибри",
                "Russian",
                "Miyagi",
                "Эндшпиль",
                "Рем", "Дигга",
                "Rap",
                "2018",
                "240",
                "23406525",
                "Я напишу про депрессуху целый том приколи мне.\n" +
                "Как улыбаться научился через силу.\n" +
                "Я бы заделался маленьким колибри.\n" +
                "И незаметно бы пропал из виду. (×2)\n" +
                " \n" +
                "Лимона нету, но всё же богат.\n" +
                "По парапету прёт настырный кот – разряд.\n" +
                "Разочарован миром этим, кто на что гаразд.\n" +
                "Сотри с лица гримасу, которая для масс.\n" +
                "Я был готов к перепадам, залив.\n" +
                "Всё то, что видел глаз, не понял мой мозг, сотри.\n" +
                "Грязи навалом в этом болоте, затих.\n" +
                "Уже не прёт против тех, кто портит правильный мотив.\n" +
                "Куда уходит мой город и совесть внутри.\n" +
                "Уже не та что говорила.\n" +
                "Брачо погоди не лги.\n" +
                "Самому себе хотя бы.\n" +
                "Запри ту дверь (бла бла бро),\n" +
                "Куда натянули грабли якобы для добра, но.\n" +
                "Пропиты души и прокурена любовь.\n" +
                "Эти игрушки доведут до дурки не хватает слов.\n" +
                "Вруби мозги, заруби на носу.\n" +
                "Пока соблазны манят, а там мороз геранят.\n" +
                "Раздором сыты твари.\n" +
                " \n" +
                "Я напишу про дипрессуху целый том приколи мне.\n" +
                "Как улыбаться научился через силу.\n" +
                "Я бы заделался маленьким колибри.\n" +
                "И незаметно бы пропал из виду. (×2)\n" +
                " \n" +
                "Погоди пацаном и кому либо там лечи, не надо басен ясень.\n" +
                "Черты сила мер затер до дыр, дымит гнилой завод.\n" +
                "А сколько демонов и повидавших Чаков Норисов.\n" +
                "В округе сколько стволов за поясом.\n" +
                "Сколько дерьма и гордости в одном флаконе.\n" +
                "А ну-ка давай-ка закати рукава.\n" +
                "И поглядим, кто кого догонит.\n" +
                "Безумству храбрых респект но не рисованных.\n" +
                "Не тем кто в падиках заблеванных (Ладно забей).\n" +
                "Сегодня Питера брадвей соберет людей.\n" +
                "MiyaGi добей куплет, ты же друг, будь добрей.\n" +
                "В этом говенном мире меня спасает улыбка ребенка.\n" +
                "Смех близкого, звонкий не гидропон (нееет).\n" +
                "Блеклые души меркнут плюс ко всему этому рушат мир.\n" +
                "До конца еще не понял о чем же трек этот.\n" +
                "Вот такой сумбур и винегрет в голове.\n" +
                "Возле Керима ей, ты не пой соловей.\n" +
                " \n" +
                "Я напишу про депрессуху целый том приколи мне.\n" +
                "Как улыбаться научился через силу.\n" +
                "Я бы заделался маленьким колибри.\n" +
                "И незаметно бы пропал из виду. (×2)\n"};
                
        String[] firstNames = new String[allElements.length/2];
        String[] lastNames = new String[allElements.length/2];
        for(int i = 0; i < allElements.length; i++)
        {
            if(i % 2 == 0)
            {
                firstNames[i/2] = allElements[i];
            }
            else
            {
                lastNames[i/2] = allElements[i];
            }
        }
        
        Map<String,String> Elements = new HashMap<>();
        for(int i = 0; i < lastNames.length; i++)
        {
            Elements.put(lastNames[i],firstNames[i]);
        }
        
        System.out.println(Elements.get("Рем"));
        //Song name
//        String song_name = "Колибри";
//        System.out.println(song_name);
//        
//        //Nationality
//        String nationality = "Russian";
//        System.out.println(nationality);
//        
//        //Artists
//        String artist1 = "Miyagi";
//        String artist2 = "Эндшпиль";
//        String artist3 = "Рем Дигга";
//        System.out.println(artist1);
//        System.out.println(artist2);
//        System.out.println(artist3);
//        
//        //Genre
//        String genre = "Rap";
//        System.out.println(genre);
//        
//        //Year Releaed
//        int release;
//        release = 2018;
//        System.out.println(release);
//        
//        //Duration
//        int duration;
//        duration = 240;
//        System.out.println(duration);
//        
//        //Number of views
//        int views;
//        views = 23406525;
//        System.out.println(views);
//        
//        //Lyrics
//        String lyrics = "Я напишу про депрессуху целый том приколи мне.\n" +
//"Как улыбаться научился через силу.\n" +
//"Я бы заделался маленьким колибри.\n" +
//"И незаметно бы пропал из виду. (×2)\n" +
//" \n" +
//"Лимона нету, но всё же богат.\n" +
//"По парапету прёт настырный кот – разряд.\n" +
//"Разочарован миром этим, кто на что гаразд.\n" +
//"Сотри с лица гримасу, которая для масс.\n" +
//"Я был готов к перепадам, залив.\n" +
//"Всё то, что видел глаз, не понял мой мозг, сотри.\n" +
//"Грязи навалом в этом болоте, затих.\n" +
//"Уже не прёт против тех, кто портит правильный мотив.\n" +
//"Куда уходит мой город и совесть внутри.\n" +
//"Уже не та что говорила.\n" +
//"Брачо погоди не лги.\n" +
//"Самому себе хотя бы.\n" +
//"Запри ту дверь (бла бла бро),\n" +
//"Куда натянули грабли якобы для добра, но.\n" +
//"Пропиты души и прокурена любовь.\n" +
//"Эти игрушки доведут до дурки не хватает слов.\n" +
//"Вруби мозги, заруби на носу.\n" +
//"Пока соблазны манят, а там мороз геранят.\n" +
//"Раздором сыты твари.\n" +
//" \n" +
//"Я напишу про дипрессуху целый том приколи мне.\n" +
//"Как улыбаться научился через силу.\n" +
//"Я бы заделался маленьким колибри.\n" +
//"И незаметно бы пропал из виду. (×2)\n" +
//" \n" +
//"Погоди пацаном и кому либо там лечи, не надо басен ясень.\n" +
//"Черты сила мер затер до дыр, дымит гнилой завод.\n" +
//"А сколько демонов и повидавших Чаков Норисов.\n" +
//"В округе сколько стволов за поясом.\n" +
//"Сколько дерьма и гордости в одном флаконе.\n" +
//"А ну-ка давай-ка закати рукава.\n" +
//"И поглядим, кто кого догонит.\n" +
//"Безумству храбрых респект но не рисованных.\n" +
//"Не тем кто в падиках заблеванных (Ладно забей).\n" +
//"Сегодня Питера брадвей соберет людей.\n" +
//"MiyaGi добей куплет, ты же друг, будь добрей.\n" +
//"В этом говенном мире меня спасает улыбка ребенка.\n" +
//"Смех близкого, звонкий не гидропон (нееет).\n" +
//"Блеклые души меркнут плюс ко всему этому рушат мир.\n" +
//"До конца еще не понял о чем же трек этот.\n" +
//"Вот такой сумбур и винегрет в голове.\n" +
//"Возле Керима ей, ты не пой соловей.\n" +
//" \n" +
//"Я напишу про депрессуху целый том приколи мне.\n" +
//"Как улыбаться научился через силу.\n" +
//"Я бы заделался маленьким колибри.\n" +
//"И незаметно бы пропал из виду. (×2)\n";
//        System.out.println(lyrics);
    }
    
}