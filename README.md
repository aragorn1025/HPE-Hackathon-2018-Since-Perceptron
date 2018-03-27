<h1>HPE AI Hackathon 2018</h1>

<h2>Syntax</h2>

* [競賽相關資訊](#hackathon_info)
* [團隊資訊](#team_info)
* [初選簡報](#first_selection_slides)
* [環境設置 (Windows)](#environment)
  * [Anaconda](#anaconda)
  * [TensorFlow (CPU verion)](#tensorflow_cpu)
  * [Keras](#keras)
* [實作](#implement)
  * 實作中，將陸續增加

* * *

<h2 id="hackathon_info">競賽相關資訊</h2>

* [HPE AI Hackathon 2018][hpe_ai_hackathon]

  [hpe_ai_hackathon]: http://www.hpe.accessus.biz/2018_HPE_AI_IoT/index.html

* * *

<h2 id="team_info">團隊資訊</h2>

* 團隊編號： 7
* 團隊名稱： Since Perceptron
* 學校：國立中央大學
* 指導老師： [蘇木春 教授][cilab]
* 團隊成員： 林○凱、唐○梅、鄭○廷、[劉○宏][4]、[戴○傑][5]

  [cilab]: http://cilab.csie.ncu.edu.tw
  [4]: https://github.com/koikoi1282
  [5]: https://github.com/aragorn1025

* * *

<h2 id="first_selection_slides">初選簡報</h2>

* [智慧燈具資料分析以改善燈具維修路線與期程][first_slides]

  [first_slides]: https://github.com/AragornDai/HPE-Hackathon-2018-Since-Perceptron/raw/master/slides/Hackathon-v2.3.pptx

* * *

<h2 id="environment">環境設置 (Windows)</h2>

以下為粗略紀錄，已確認於 Mircosoft Windows 7 或 Mircosoft Windows 10 上安裝成功

<h3 id="anaconda">Anaconda</h3>

以下為粗略紀錄，將安裝 [Anaconda 5.1 For Windows Installer Python 3.6 version][anaconda_5_1_python_3_6] ，更新版本可至 [Anaconda官方網站][anaconda_download] 下載

1. 為了避免安裝失敗，先將環境變數 <code>Path</code> 的名稱修改為 <code>PathBak</code>
2. [下載 Anaconda][anaconda_download] ，在此將安裝 [Anaconda 5.1 For Windows Installer Python 3.6 version][anaconda_5_1_python_3_6]
3. 可視情況安裝於當前使用者，或是改選安裝於所有使用者 (All User)
4. 進階選項 (Advanced Options) 步驟中，勾選將 Anaconda 加入到 <code>Path</code> 環境變數 (Add Anaconda to my PATH environment variable) ，此步驟將會影響 <code>Path</code> 環境變數，為了避免安裝失敗，務必確認第一步驟已執行
5. 等待安裝完成
6. 將環境變數修改回來：此時會看到 <code>Anaconde</code> 新增的 <code>Path</code> 及第一步修改的 <code>PathBak</code> ，將 <code>PathBak</code> 的值複製，並且加在 <code>Path</code> 的值之後，看起來應該會像
   <pre><code>C:\ProgramData\Anaconda3;C:\ProgramData\Anaconda3\Library\mingw-w64\bin;C:\ProgramData\Anaconda3\Library\usr\bin;C:\ProgramData\Anaconda3\Library\bin;C:\ProgramData\Anaconda3\Scripts; ......</code></pre>
7. 將環境變數 <code>PathBak</code> 刪除
8. 測試安裝是否成功：啟動 <code>CMD</code> ，並且輸入 <code>conda --version</code>
9. 若是成功安裝將會看到 <code>Conda</code> 版本號碼

  [anaconda_download]: https://www.anaconda.com/download/
  [anaconda_5_1_python_3_6]: https://repo.continuum.io/archive/Anaconda3-5.1.0-Windows-x86_64.exe

<h3 id="tensorflow_cpu">TensorFlow (CPU version)</h3>

1. 安裝 [<code>Anaconda</code>][readme_anaconda]
2. 建立 <code>tensorflow</code> <code>anaconda</code> 虛擬環境：啟動 <code>CMD</code> ，並且輸入
   <pre><code>conda create --name tensorflow python=3.5 anaconda</code></pre>
3. <code>Conda</code> 將詢問是否安裝列表中的套件，按下 <code>y</code>，並等待套件安裝完成
4. 啟動 <code>anaconda</code> 虛擬環境：安裝完成後，繼續於 <code>CMD</code> 中輸入
   <pre><code>activate tensorflow</code></pre>
5. 安裝 <code>TensorFlow CPU</code> 版本：於 <code>tensorflow</code> 虛擬環境下，輸入
   <pre><code>pip install tensorflow</code></pre>
6. 啟動 <code>Python</code> 虛擬環境：繼續於 <code>tensorflow</code> 虛擬環境下，輸入
   <pre><code>python</code></pre>
7. 測試安裝是否成功：於 <code>python</code> 虛擬機中輸入
   <pre><code>import tensorflow as tf</code></pre>
  * 可能會出現 <code>FutureWarning</code>，目前已知為部分套件未來將升級而跳出的警告，並不會影響後續的程式碼執行，請不用擔心
8. 接著於 <code>python</code> 虛擬機中輸入
   <pre><code>tf.__version__</code></pre>
9. 若是成功安裝將會看到 <code>TensorFlow</code> 版本號碼

<h3 id="keras">Keras</h3>

1. 安裝 [<code>Anaconda</code>][readme_anaconda]
2. 安裝 [<code>TensorFlow (CPU version)</code>][readme_tensorflow_cpu]
3. 啟動 <code>anaconda</code> 虛擬環境：安裝完成後，於 <code>CMD</code> 中輸入
   <pre><code>activate tensorflow</code></pre>
4. 安裝 <code>Keras</code> ：於 <code>tensorflow</code> 虛擬環境下，輸入
   <pre><code>pip install keras</code></pre>
5. 啟動 <code>Python</code> 虛擬環境：於 <code>tensorflow</code> 虛擬環境下，輸入
   <pre><code>python</code></pre>
6. 測試安裝是否成功：於 <code>python</code> 虛擬機中輸入
   <pre><code>import tensorflow as tf</code></pre>
  * 可能會出現 <code>FutureWarning</code>，目前已知為部分套件未來將升級而跳出的警告，並不會影響後續的程式碼執行，請不用擔心
7. 接著於 <code>python</code> 虛擬機中輸入
   <pre><code>import keras</code></pre>
8. 接著於 <code>python</code> 虛擬機中輸入
   <pre><code>keras.__version__</code></pre>
9. 若是成功安裝將會看到 <code>Keras</code> 版本號碼

[readme_anaconda]: https://github.com/AragornDai/HPE-Hackathon-2018-Since-Perceptron/blob/master/README.md#anaconda
[readme_tensorflow_cpu]: https://github.com/AragornDai/HPE-Hackathon-2018-Since-Perceptron/blob/master/README.md#tensorflow_cpu

* * *

<h2 id="implement">實作</h2>

實作中，將陸續增加
