# Vue3+Flask实现前后端分离计算器

[toc]

| 这个作业属于哪个课程 | [2301-计算机学院-软件工程社区-CSDN社区云](https://bbs.csdn.net/forums/ssynkqtd-05?typeId=5171424) |
| -------------------- | ------------------------------------------------------------ |
| 这个作业要求在哪里   | [第二次作业--前后端交互计算器-CSDN社区](https://bbs.csdn.net/topics/617377308) |
| 这个作业的目标       | 实现前后端分离的计算器                                       |
| 其他参考文献         | Vue3中文文档https://cn.vuejs.org/guide/introduction.html，案例参考[06 flask+vue前后端全分离_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1zB4y1v7wN/?p=6&spm_id_from=333.880.my_history.page.click&vd_source=4f24f3057448527deda5427be06a7763)，Flask框架学习[2023版-零基础玩转Python Flask框架-学完可就业_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV17r4y1y7jJ/?spm_id_from=333.337.search-card.all.click)，Vue3项目学习[Day2-10.项目起步-项目整体路由设计_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1Ac411K7EQ/?p=26&spm_id_from=333.880.my_history.page.click)，JavaScript基础学习[5、严格检查模式strict_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1JJ41177di/?p=5&spm_id_from=333.880.my_history.page.click&vd_source=4f24f3057448527deda5427be06a7763) |

## Gitcode项目地址

前端代码项目地址：[NightMare33133/102101342_calculator_frontend (github.com)](https://github.com/NightMare33133/102101342_calculator_frontend)

后端代码项目地址：[NightMare33133/102101342_calculator_backend (github.com)](https://github.com/NightMare33133/102101342_calculator_backend)

## PSP表格

| PSP                                     |        Personal Software Process Stages | 预估耗时（分钟） | 实际耗时（分钟） |
| :-------------------------------------- | --------------------------------------: | :--------------: | ---------------- |
| Planning                                |                                    计划 |        60        | 60               |
| • Estimate                              |              • 估计这个任务需要多少时间 |        30        | 30               |
| Development                             |                                    开发 |       2700       | 3100             |
| • Analysis                              |            • 需求分析 (包括学习新技术） |       1500       | 1700             |
| • Design Spec                           |                          • 生成设计文档 |        30        | 30               |
| • Design Review                         |                              • 设计复审 |        30        | 30               |
| • Coding Standard                       | • 代码规范 (为目前的开发制定合适的规范) |        30        | 30               |
| • Design                                |                              • 具体设计 |        60        | 60               |
| • Coding                                |                              • 具体编码 |       930        | 1130             |
| • Code Review                           |                              • 代码复审 |        60        | 60               |
| • Test                                  |  • 测试（自我测试，修改代码，提交修改） |        60        | 60               |
| Reporting                               |                                    报告 |       180        | 180              |
| • Test Report                           |                              • 测试报告 |        30        | 30               |
| • Size Measurement                      |                            • 计算工作量 |        30        | 30               |
| • Postmortem & Process Improvement Plan |          • 事后总结, 并提出过程改进计划 |       120        | 120              |
|                                         |                                    合计 |       2940       | 3340             |

## 作业要求

#### 1、基础计算器功能

- 功能1：加减乘除、取余、括号运算
  - 基础+，-，* ，/，%，（）运算，要求运算顺序正确，结果正确，**并将输入的字符串和结果存储到后端数据库中**
- 功能2：清零回退
  - 实现字符串输入的清零和回退功能
- 功能3：错误提示
  - 在第一个功能正常的情况下增加非法输入提示，例如：0不能作为除数，括号不匹配等
- 功能4：读取历史记录
  - 能用ans按钮返回上一个计算结果，并且查看历史记录读取最后十个字符串式子和对应的计算结果， **必须从后端的数据库中读取，不能使用缓存**
- 附加功能1：科学计算器
  - 计算根号、三角函数、log、科学计数法、微积分等附加功能
- 附加功能2：页面原型设计
  - 页面设计复现越接近现有的计算器页面，附加分越高
- 附加功能3：项目部署
  - 在博客中给出项目部署到云服务器后的**访问链接**

#### 2、利率计算器功能

**功能1：计算存款、贷款利息**

- 实现利率计算器，数据库中存储利率表（可随时修改利率），对应利率如下图所示。要求：用两个输入框分别读取前端的输入数据，1.输入存款/贷款金额，2.存/贷时长（单位：年）。输出计算后对应的存/贷利息。**注意：前端利率计算时，需要从后端获取这个利率表，不能在前端的某个变量也存储这个利率表**
- **扩展功能：前端修改存贷款利息**
  - 要求在前端页面输入被修改的信息，数据库中表的数值相应修改
  - 输入要求：1.存款/贷款 2.时长（单位：年）3.修改后的利率
  - 运行结果：在数据库的表中相应位置的数据更新

## 解题思路描述

 此次作业要求我们将上次作业实现的计算器做成前后端分离的形式，由于对于前后端分离如何实现不太明白，光是为了理解如何实现这句话就恶补了不少前后端相关的知识才明白要怎么做。由于先前作业的实现选择了python，于是我继续选择python实现本次作业的后端，从Django和flask中选择比较轻量级的flask作为后端的框架进行学习。在了解后端如何运作后，发现flask相关的前后端分离的项目案例视频较少，最终选中了vue3作为前端框架进行学习。

总之，先是进行了一定量对于后端Flask框架的基础知识的学习，然后在对接数据库也跟着视频教学中选择了Mysql作为数据库进行存储，同时接触到少量的前端中的HTML，CSS，JavaScript的相关代码后，就干脆先简单学习了前端语言HTML，CSS，JavaScript的部分简单基础课，才开始选择前端的框架进行学习，在选择Vue3框架的项目案例的选择使用的Vue3框架中的JS相关的代码又与先前学习的JS代码不太一样，后续才发现，Vue3框架所使用的JS代码运用了组合式API并且与<script setup>搭配使用，这是一个一定程度上简化JS代码的语法糖，但是很尴尬的是基础JS的代码也学艺不精，就只能硬着头皮嗯啃了，总之是磕磕绊绊的把大部分要求的功能实现了。

## 前端页面展示

以下为前端计算器页面的展示

![前端页面展示](.\pic\前端页面展示.png)

以下为前端利率计算器页面的展示（这个较为匆忙就做得比较随意了0.0）

![前端利率计算器页面展示](.\pic\前端利率计算器页面展示.png)

## 功能展示

### 计算器展示

##### 功能1：加减乘除、取余、括号运算

- 基础+，-，* ，/，%，（）运算，要求运算顺序正确，结果正确，**并将输入的字符串和结果存储到后端数据库中**

  总之把要求的运算都来了一遍

  ![功能1演示](.\pic\功能1演示.gif)

##### 功能2：清零回退

![功能2](.\pic\功能2.gif)

##### 功能3：错误提示

![功能3](.\pic\功能3.gif)



##### 功能4：读取历史记录

（功能1中一起展示了数据库，就直接用下功能1的图了0.0）

![功能4](.\pic\功能4.gif)

![功能1演示](.\pic\功能1演示.gif)

##### 附加功能1：科学计算器

![附加功能1](.\pic\附加功能1.gif)

##### 附加功能2：页面原型设计

![页面原型设计](.\pic\页面原型设计.png)

### 利率计算器展示

##### 功能1：计算存款、贷款利息

![利率功能1](.\pic\利率功能1.gif)

**扩展功能：前端修改存贷款利息**

![利率计算器功能2](.\pic\利率计算器功能2.gif)

## 关键代码展示

 首先是找了一个前端计算机项目当作框架进行学习，然后基于自身需求理解其中的代码进行改动，做出了前端的计算器界面

###  计算器相关代码展示

#### 以下为计算器的html的相关代码

具体用于布局的css相关代码项目仓库中的具体文件calculator.vue中可以找到，其中按钮通过@click绑定到对应的js函数，点击后触发对应的事件，{{变量}}为vue框架中加入js变量的代码

```
<td>
  <div class="calculator">
    <div class="result" style="grid-area: result">
      {{ display_equation }}
    </div>

    <button style="grid-area: clear" @click="clear">C</button>
    <button style="grid-area: percent" @click="append('%','%')">%</button>
    <button style="grid-area: back" @click="back">←</button>
    <button style="grid-area: add" @click="append('+','+')">+</button>
    <button style="grid-area: subtract" @click="append('-','-')">-</button>
    <button style="grid-area: multiply" @click="append('*','×')">×</button>
    <button style="grid-area: divide" @click="append('/','÷')">÷</button>
    <button style="grid-area: equal" @click="calculate">=</button>
    <button style="grid-area: sin" @click="append('sin','sin')">sin</button>
    <button style="grid-area: cos" @click="append('cos','cos')">cos</button>
    <button style="grid-area: tan" @click="append('tan','tan')">tan</button>
    <button style="grid-area: Left_bracket" @click="append('(','(')">(</button>
    <button style="grid-area: Right_bracket" @click="append(')',')')">)</button>
    <button style="grid-area: Log10" @click="append('log10','log10')">log10</button>
    <button style="grid-area: Ans" @click="Ans">Ans</button>
    <button style="grid-area: π" @click="append('pi','π')">π</button>
    <button style="grid-area: √" @click="append('sqrt','sqrt')">√</button>
    <button style="grid-area: pow" @click="append('**','^')">^</button>


    <button style="grid-area: number-1" @click="append(1,1)">1</button>
    <button style="grid-area: number-2" @click="append(2,2)">2</button>
    <button style="grid-area: number-3" @click="append(3,3)">3</button>
    <button style="grid-area: number-4" @click="append(4,4)">4</button>
    <button style="grid-area: number-5" @click="append(5,5)">5</button>
    <button style="grid-area: number-6" @click="append(6,6)">6</button>
    <button style="grid-area: number-7" @click="append(7,7)">7</button>
    <button style="grid-area: number-8" @click="append(8,8)">8</button>
    <button style="grid-area: number-9" @click="append(9,9)">9</button>
    <button style="grid-area: number-0" @click="append(0,0)">0</button>

    <button style="grid-area: dot" @click="append('.','.')">.</button>
  </div>
</td>
```

#### 以下为计算器的JS相关代码以及部分flask后端代码

我的js代码可能不太一样，是我用了vue3的语法糖的缘故

以下两段代码是用于不断刷新界面更新历史记录的代码，这里的fetch与传统js的ajax发送请求应该比较类似。

总之以下代码就是向后端接口/history规律性的发送请求更新页面

```javascript
const fetchData = () => {
  fetch('http://127.0.0.1:5000/history').then(res => {
    return res.json();
  }).then((data)=>{
    console.log(data);
    equation2.value = data;
    console.log(equation2)
  });
}
```

```javascript
onMounted(() => {
  fetchData();
});
```

#####  以下为flask的对应接口的代码

从数据库中获取历史记录信息并将字典加入列表，并json化后发送给访问接口的请求

```python
@app.route('/history', methods=['GET', 'POST'])
def history():
    if request.method == 'GET':
        count = 0
        his = History.query.all()
        his.reverse()
        history_list = []
        for i in his:
            res = {"id":i.id,"result":i.history}
            history_list.append(res)
            count = count + 1
            if count == 10 :
                break
        #print(history_list)
        return jsonify(history_list)
```

##### 以下js代码为按按钮后将信息传入屏幕的功能

计算器按数字键以及公式键位后为显示屏添加字符，其中两个参数分别加入两段字符串，一段是屏幕显示的字符串，一段是隐藏起来发送到后端实际运算的字符串

```javascript
const append = (character,dis_character) => {
  if(equation.value == "" && display_equation.value != ""){
    display_equation.value = "";
  }

  display_equation.value = display_equation.value + dis_character;
  equation.value = equation.value + character;
}
```

##### 以下为C键的清除功能

```
const clear = () => {
  equation.value = "";
  display_equation.value = "";
}
```

##### 以下为back键的清除功能

如果不区分实际显示字符串和公式字符串的话，退格键大概只需要以下这段代码

equation.value = equation.value.split("").slice(0, -3).join("");

但是我之前python也是分显示和eval能识别的两种字符串，不过这样搞会导致退格键实现变得比较麻烦，因为退格的时候实际显示的是2个字符，后面可能有3个字符，而且sin，cos这类三角函数最好一口气删掉不然一格一格退就会出现英文字母单走的情况。

```
const back = () => {
  let char = equation.value.slice(-1);
  console.log(char);
  let Arr = ["n","s","0",'g','i','t','*'];
  for (let i in Arr)
  {
    if(char == Arr[i])
    {
      switch (char){
        case 'n':
          equation.value = equation.value.split("").slice(0, -3).join("");
          display_equation.value = display_equation.value.split("").slice(0, -3).join("");
          return;
        case 's':
          equation.value = equation.value.split("").slice(0, -3).join("");
          display_equation.value = display_equation.value.split("").slice(0, -3).join("");
          return;
        case '0':
          let t = equation.value.slice(-5);
          if(t == 'log10'){
            equation.value = equation.value.split("").slice(0, -5).join("");
            display_equation.value = display_equation.value.split("").slice(0, -5).join("");
            return;
          }
          else break;
        case 'g':
          equation.value = equation.value.split("").slice(0, -3).join("");
          display_equation.value = display_equation.value.split("").slice(0, -2).join("");
          return
        case 'i':
          equation.value = equation.value.split("").slice(0, -2).join("");
          display_equation.value = display_equation.value.split("").slice(0, -1).join("");
          return;
        case 't':
          equation.value = equation.value.split("").slice(0, -4).join("");
          display_equation.value = display_equation.value.split("").slice(0, -4).join("");
          return;
        case '*':
          let t1 = equation.value.slice(-2);
          if(t1=="**"){
            equation.value = equation.value.split("").slice(0, -2).join("");
            display_equation.value = display_equation.value.split("").slice(0, -1).join("");
            return;
          }
          else break;

      }
    }
  }
  equation.value = equation.value.split("").slice(0, -1).join("");
  display_equation.value = display_equation.value.split("").slice(0, -1).join("");
}
```

##### 以下为Ans功能键的实现

这里是访问了后端的/Ans接口以返回上一次计算结果的值

```
const Ans = () => {
  fetch('http://127.0.0.1:5000/Ans').then(res => {
    return res.json();
  }).then((data)=>{
    console.log(data);
    display_equation.value = display_equation.value + data.result;
    equation.value = equation.value + data.result;
  });
}
```

##### 以下为Ans键对应的后端接口代码

就是从数据库直接找最新的一条记录然后split取等于号后面的字符串

```
@app.route('/Ans', methods=['GET', 'POST'])
def Ans():
    if request.method == 'GET':
        his = History.query.all()
        res = his[-1].history
        result = res.split("=")[-1]
        return {'result': result}
```

##### 以下为equation键触发后计算结果的js代码

其实就是把两个算术式字符串发到后端去，屏幕显示的存到数据库中，实际运算的算式发给后端算

```
const calculate= () => {
  let vl = {
    result:equation.value,
    dis_result:display_equation.value
  };
  fetch('http://127.0.0.1:5000/calculate', {
    method: 'POST',
    body: JSON.stringify(vl),
    headers: {'Content-Type': 'application/json'},
  }).then((response) =>{
    return response.json();
  }).then((data) => {
    console.log(data);
    equation.value = '';
    display_equation.value = data.result
    fetchData();
  });
}
```

至此计算机功能的代码应该差不多都讲完了。

### 利率计算器相关代码展示

#### 以下为利率计算器的html代码

这里面其实也就是button中对应的@click去触发js代码，然后这里多学会用了个select和option的html标签可以做做选择题

```
<template>
  <div class="rate_calculator">

    <table style="margin: 0px auto;width: 140px;border-right: 1px solid #000000;
        border-bottom: 1px solid #000000;
        text-align: center;">
      <caption style="font-size: 22px;">存款利率表</caption>
      <tr style="border-left: 1px solid #000000;
        border-top: 1px solid #000000;" v-for="msg in rate_msg">
        <td style="border-left: 1px solid #000000;
        border-top: 1px solid #000000;" v-if="msg.type">{{msg.time}}</td>
        <td style="border-left: 1px solid #000000;
        border-top: 1px solid #000000;" v-if="msg.type">{{msg.rate}}</td>
      </tr>
    </table>
      <caption style="font-size: 20px;">存款利息计算器</caption>
      <tr>
        <td>整存整取定期存款：</td><td>存款金额</td><td><input type="text" id="Deposit_amount"></td>
        <td>存款时长</td>
        <select style="width: 150px;" id="Deposit_time">
          <option>三个月</option>
          <option>半年</option>
          <option>一年</option>
          <option>三年</option>
          <option>五年</option>
        </select>
        <td>
          <button @click="get_deposit_interest">获取存款利息结果</button>
        </td>
      </tr>
      <tr>
        <td>活期存款：</td><td>存款金额</td><td><input type="text" id="Deposit_amount1"></td>
        <td>存款时长</td><input type="text" style="width: 30px;" id="Deposit_time1">年(填入阿拉伯数字)
        <td>
          <button @click="get_deposit_interest1">获取存款利息结果</button>
        </td>
      </tr>
    <table>
      <tr>
        <td>整存整取定期存款利息:</td><td>{{deposit_interest}}</td>
      </tr>
    </table>
    <table>
      <tr>
        <td>活期存款利息:</td><td>{{deposit_interest1}}</td>
      </tr>
    </table>

    <table style="margin: 0px auto;width: 140px;border-right: 1px solid #000000;
        border-bottom: 1px solid #000000;
        text-align: center;">
      <caption style="font-size: 22px;">贷款利率表</caption>
      <tr style="border-left: 1px solid #000000;
        border-top: 1px solid #000000;" v-for="msg in rate_msg">
        <td style="border-left: 1px solid #000000;
        border-top: 1px solid #000000;" v-if="!msg.type">{{msg.time}}</td>
        <td style="border-left: 1px solid #000000;
        border-top: 1px solid #000000;" v-if="!msg.type">{{msg.rate}}</td>
      </tr>
    </table>
    <table style="margin: 0px auto;">
      <caption style="font-size: 20px;">贷款利息计算器</caption>
      <tr>
        <td>贷款金额</td><td><input type="text" id="Loan_amount"></td>
        <td>贷款时长</td>
        <input type="text" style="width: 30px;" id="Loan_time">年(填入阿拉伯数字)
        <td>
          <button @click="get_loan_interest">获取贷款利息结果</button>
        </td>
      </tr>
      <tr>
        <td>贷款利息:</td><td>{{loan_interest}}</td>
      </tr>
    </table>

    <table style="margin: 0px auto;">
      <caption style="font-size: 20px;width: 200px" >存贷款利率修改</caption>
      <tr>
        <td>
          存/贷款
            <select id="change_type" style="width: 60px;">
              <option>贷款</option>
              <option>存款</option>
            </select>
        </td>
      </tr>
      <tr>
        <td>
          存/贷款时长
          <select id="change_time" style="width: 90px;">
            <option>活期存款</option>
            <option>三个月</option>
            <option>半年</option>
            <option>六个月</option>
            <option>一年</option>
            <option>一至三年</option>
            <option>三年</option>
            <option>三至五年</option>
            <option>五年</option>
          </select>
        </td>
      </tr>
      <tr>
        <td>修改后利率
          <input type="text" style="width: 50px" id="change_rate">
        </td>
      </tr>
      <tr>
        <td>
          <button @click="change_rate" >修改</button>
        </td>
      </tr>
    </table>

  </div>
</template>
```

#### 以下为利率计算器的js代码和相关后端flask代码

##### 以下为更新利率表的js代码

这里是直接和历史记录极其相似的代码，用于刷新利率表数值的，这里是向后端接口/get_rate_msg发送请求

```
const fetchData = () => {
  fetch('http://127.0.0.1:5000/get_rate_msg').then(res => {
    return res.json();
  }).then((data)=>{
    console.log(data);
    rate_msg.value = data
    
  });
}
```

```
onMounted(() => {
  fetchData();
});
```

##### 以下为python中的对应接口的flask代码

与历史记录类似我就不多赘述了

```
@app.route('/get_rate_msg', methods=['GET', 'POST'])
def get_rate_msg():
    if request.method == 'GET':
        D_table = Deposit_interest_Rate.query.all()
        list = []
        for i in D_table:
            res = {"id":i.id,"time":i.time,"rate":format(i.rate, '.2f'),"type":True}
            list.append(res)
        L_table = Loan_interest_Rate.query.all()
        for i in L_table:
            res = {"id":i.id,"time":i.time,"rate":format(i.rate, '.2f'),"type":False}
            list.append(res)


        return jsonify(list)
```

##### 以下是计算存款利率的js代码

这里就是触发按钮后，利用getElementById函数从按钮前面的两个框中获取time和amoun的数值（要在对应的标签中打入例如id="Deposit_amount"才能通过id从中获取参数），然后将数值发送给后端接口/get_deposit_interest，并将返回值直接更改到变量deposit_interest以实现计算存款利率的功能

ps：存款利率的定期存款和贷款利率也是类似的，后续就不多展示了

```
const get_deposit_interest= () => {
  let amount = document.getElementById('Deposit_amount');
  let time = document.getElementById('Deposit_time');
  let vl = {
    amount:amount.value,
    time:time.value
  };
  console.log(vl);
  fetch('http://127.0.0.1:5000/get_deposit_interest', {
    method: 'POST',
    body: JSON.stringify(vl),
    headers: {'Content-Type': 'application/json'},
  }).then((response) =>{
    return response.json();
  }).then((data) => {
    console.log(data);
    deposit_interest.value = data.result;
  });
}
```

##### 以下为python中的对应接口的flask代码

从数据库中取得rate的数值，再与发送过来的数值进行计算，由于我直接用选项框，所以用了if分支来处理amount信息

```
@app.route('/get_loan_interest', methods=['GET', 'POST'])
def get_loan_interest():
    if request.method == 'POST':
        time = request.json.get('time')
        amount = request.json.get('amount')
        time = float(time)
        if time <= 0.5:
            msg = Loan_interest_Rate.query.filter_by(time="六个月").first()
        elif time >0.5 and time <= 1:
            msg = Loan_interest_Rate.query.filter_by(time="一年").first()
        elif time >1 and time <= 3:
            msg = Loan_interest_Rate.query.filter_by(time="一至三年").first()
        elif time >3 and time <= 5:
            msg = Loan_interest_Rate.query.filter_by(time="三至五年").first()
        elif time >5:
            msg = Loan_interest_Rate.query.filter_by(time="五年").first()

        result = str(msg.rate * 0.01) + "*" + str(float(amount)) + "*" +str(time)
        result = eval(str(result))
        result = format(result, '.2f')
    return {'result': result}
```

##### 以下是修改利率的js代码

这里是发送了put请求，大致与计算利率的差别不太大，不过多发送了一个type类型用于分辨是存款还是贷款，其实这里的html代码存在一定缺陷，我的选项框没有把时间给区分出来，本来是想着选择贷款后跳出的选项框是贷款对应的这样，但是时间有点不太多了，只能先赶赶工了。

```
const change_rate= () => {
  let rate = document.getElementById('change_rate');
  let time = document.getElementById('change_time');
  let type = document.getElementById('change_type');
  let vl = {
    rate:rate.value,
    time:time.value,
    type:type.value
  };
  console.log(vl);
  fetch('http://127.0.0.1:5000/change_rate', {
    method: 'PUT',
    body: JSON.stringify(vl),
    headers: {'Content-Type': 'application/json'},
  }).then((response) =>{
    return response.json();
  }).then((data) => {
    console.log(data);
    fetchData();
  });
}
```

##### 以下为python中的对应接口的flask代码

用if else判断一下type类型，然后用filter筛选出符合的数据并用update进行更新，这个update可以尽可能避免并发情况下发送多次请求却漏更新数值的情况

```
@app.route('/change_rate', methods=['PUT'])
def change_rate():
    if request.method == 'PUT':
        time = request.json.get('time')
        rate = request.json.get('rate')
        type = request.json.get('type')
        if type == "贷款":
            Loan_interest_Rate.query.filter(Loan_interest_Rate.time==time).update({"rate":rate})
        elif type == "存款":
            Deposit_interest_Rate.query.filter(Deposit_interest_Rate.time==time).update({"rate":rate})
        db.session.commit()
        return {'result': "修改成功"}
```

### 数据库模型信息

```
class History(db.Model):
    __tablename__ = "history"
    id = db.Column(db.Integer, primary_key=True, comment='自动递增id，唯一键')
    history = db.Column(db.String(120), nullable=False, comment='历史记录')

class Deposit_interest_Rate(db.Model):
    __tablename__ = "Deposit_interest_Rate"
    id = db.Column(db.Integer, primary_key=True, comment='自动递增id，唯一键')
    time = db.Column(db.String(120), nullable=False, comment='存款时长')
    rate = db.Column(db.Double, nullable=False, comment='存款利率')

class Loan_interest_Rate(db.Model):
    __tablename__ = "Loan_interest_Rate"
    id = db.Column(db.Integer, primary_key=True, comment='自动递增id，唯一键')
    time = db.Column(db.String(120), nullable=False, comment='贷款时长')
    rate = db.Column(db.Double, nullable=False, comment='贷款利率')
```

## 心得体会

​        说实话，这一次的作业真的比上一次麻烦太多太多了，真的是做得心态有点要炸了，虽然计算器实际实现的功能和之前算是差不多的，但是讲真的，各种参数的传递，术语的理解，什么前端后端，什么事件触发，各种乱七八糟的东西学起来真的是太复杂了，对应前后端相关几乎没啥基础学起来是相当的麻烦，因为真的去把flask，vue3，html，css，javascript相关代码的基础全看完再来做的话，讲实话真的来不及做，不过实话也是自己没那么大的耐心去看完（只能说菜鸡是这样的），只能简单啃一点点基础，然后自己上手做一些小测试把玩一下这个代码会发生什么事情，学得好像够用了，才开始做这个作业，然后就是边学边加入功能的过程，不断的调试修改，最终做出来的成品说实话也就是普普通通（只能说基础差是这样的）说真的，要是真的上周就要交的话，以我的0基础根本来不及做出来这个作业了/(ㄒoㄒ)/~~

​      不过经过这段时间的折磨也算是真的学到了还算不少的知识吧，至少勉勉强强算是对于前后端的知识入门了？虽然还是很多很多东西不明白，但还是继续努努力吧！