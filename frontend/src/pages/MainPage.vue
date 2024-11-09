
<template>
      <v-main>
      <v-container id='main-container'>
        <v-row
        id='first-main'

        class='main-card'>
          <v-col
            width="300"
            cols=columnCount
          >
          <v-lazy
            v-if="kLogoDelay"
            :options="{
              threshold: .00000001
            }"
            min-height="50"
            transition="fade-transition"
          >
            <img v-if="kLogoDelay" id="main-logo" src="../assets/img/logo_transparent.png" alt="avatar" />
          </v-lazy>
                                  <br />
                                  <br />
            <v-lazy
              v-if="logoDelay"
              :options="{
                threshold: .00000001
              }"
              min-height="200"
              transition="fade-transition"
            >
            <figure>
              <img src="../assets/img/nti-logo.svg" alt="avatar" />
            </figure>
            </v-lazy>
                        <br />
                        <br />
                        <br />
                        <br />
            <v-lazy
              v-if="titleDelay"
              :options="{
                threshold: .00000001
              }"
              min-height="200"
              transition="fade-transition"
            >
            <h1>
              Развитие сервиса персональных траекторий развития — создание модели, анализирующей образовательные и карьерные цели человека
            </h1>
          </v-lazy>
          </v-col>
        </v-row>
        <v-row
        id='second-main'
        class='main-card'>
          <v-col
            width="300"
            cols=columnCount
          >
            <div >
              <p>
                <b>Технология SMART (СМАРТ)</b> — современный подход к постановке работающих целей. Система постановки smart — целей позволяет на этапе целеполагания обобщить всю имеющуюся информацию, установить приемлемые сроки работы, определить достаточность ресурсов, предоставить всем участникам процесса ясные, точные, конкретные задачи.

              </p>
                    <v-lazy
                      :options="{
                        threshold: .1
                      }"
                      min-height="200"
                      transition="fade-transition"
                    >
                <v-sparkline
                  :value="value"
                  :gradient="gradient"
                  :smooth="radius || false"
                  :padding="padding"
                  :line-width="width"
                  :stroke-linecap="lineCap"
                  :gradient-direction="gradientDirection"
                  :fill="fill"
                  :type="type"
                  :auto-line-width="autoLineWidth"
                  auto-draw
                ></v-sparkline>
              </v-lazy>
            <p>
                <b>SMART</b> является аббревиатурой, расшифровка которой: Specific, Measurable, Achievable, Relevant, Time bound. Каждая буква аббревиатуры SMART означает критерий эффективности поставленных целей. Рассмотрим каждый критерий smart цели более подробно.

              </p>

            </div>
          </v-col>
        </v-row>
        <v-row
        id='third-main'
        class='main-card'>
          <v-col
            width="300"
            cols=columnCount
          >
          <div >
            <p>
              <span>
                S
              </span>
              <br />
              <b>Specific</b> —<br /> конкретной. Конкретика означает, что результатом формулировки цели
              является ответ на вопрос: «что сделать?». Варианты: Чего добиться? Где? Когда? С кем?
              В каком объеме? и т.д. В постановке цели не должно быть слов, не несущих смысловой нагрузки
              (оптимальный, достойный и т.п.), никаких расплывчатых и двусмысленных формулировок.
            </p>
            <p>
              <span>
                M
              </span>
              <br />
              <b>Measurable</b> —<br /> измеримой. Как ты узнаешь, что уже достиг своей цели? И в какой степени
              ты ее достиг? Если речь идет о количественной измеримости, нужно оперировать цифрами, если о
              качественной - к формулировке цели следует приложить задание.
            </p>
            <p>
              <span>
                A
              </span>
              <br />
              <b>Achievable</b> —<br /> достижимой. Например, цель "стать профессионалом в хирургии за 3 месяца"
              едва ли достижима. В этом пункте важно трезво учесть профессиональные и личные качества, при этом можно
              себе ставить достаточно высокую «планку» и ориентироваться на напряженный ритм работы.
            </p>
            <p>
              <span>
                R
              </span>
              <br />
              <b>Result-oriented</b> —<br /> ориентированной на Результат. А не на процесс.
              <br />
              <img src="../assets/img/goal.jpg" alt="avatar" />
            </p>
            <p>
              <span>
                T
              </span>
              <br />
              <b>Time-limited</b> — <br /> ограниченной по времени. При постановке цели важно определить конечный
              срок, а также учесть, что формулировка вроде
              «выполнить в течение 30 дней» ориентирует скорее на процесс, чем на результат.
              А цель "до 17 марта обзвонить и проинформировать 100 клиентов из базы данных,
              родить двух детей до 30 лет" - дает разумное ограничение по времени.
              Важно указать крайний срок ее исполнения (dead-line).
            </p>

            </p>
          </div>
            <div>
              <p>
                <img class="attr-image" src="../assets/img/mortarboard.svg" alt="avatar" />
                <b>Образование</b> представляет собой основной компонент развития. Оно расширяет возможности людей и является ключом к достижению целей.
              </p>
              <p>

              </p>
              <p>
                <img class="attr-image" src="../assets/img/precision.svg" alt="avatar" />
                  Правильная цель должна быть очень крутой и давать заряд счастья. Цель становится эффективной только тогда, когда затрагивает ваши чувства. Она <b>однозначна</b> и непоколебима.
              </p>
            </div>
          </v-col>
        </v-row>
          <v-fab-transition>
            <v-btn
              color="pink"
              dark
              fixed
              right
              bottom
              fab
              @click="$vuetify.goTo('#four-main')"
              >
                GO
              </v-btn>
            </v-fab-transition>
        <v-row
        id='four-main'
        class='main-card'>
          <v-col
            v-if="showResult"
            width="300"
            cols=columnCount
          >
            <div >
              <svg viewBox="0 0 130 130" fill="none" xmlns="http://www.w3.org/2000/svg" class="little mXlbn"><path d="M130 65.7201v-1.4402c-28.809-.9002-41.9439-1.5843-52.4411-11.837C67.3137 41.9471 66.5845 28.7779 65.7202 0h-1.4404c-.9003 28.8049-1.5845 41.9471-11.8387 52.4429C41.9439 62.6956 28.7819 63.4157 0 64.2799v1.4402c28.8089.9002 41.9439 1.5843 52.4411 11.837C62.6953 88.0529 63.4155 101.222 64.2798 130h1.4404c.9003-28.805 1.5935-41.9471 11.8387-52.4429C88.0561 67.3044 101.218 66.5843 130 65.7201z" fill="white"></path></svg>
                <h2>
                  ВВЕДИ СВОЮ ЦЕЛЬ
                </h2>
                <br />
                <p>
                  Наша система определит насколько твоя цель соответвует критериями смарт и поможет правильно её сформулировать
                </p>
              <v-textarea
                v-model="query"
                solo
                name="input-7-4"
                label="до 17 марта обзвонить и проинформировать 100 клиентов из базы данных"
                auto-grow
              ></v-textarea>
              <p>

              <v-btn
                class="ma-2"
                :loading="loading"
                :disabled="loading"
                color="secondary"
                @click="loader = 'loading'"
              >
                ОТПРАВИТЬ
              </v-btn>
                <svg viewBox="0 0 130 130" fill="none" xmlns="http://www.w3.org/2000/svg" class="big mXlbn"><path d="M130 65.7201v-1.4402c-28.809-.9002-41.9439-1.5843-52.4411-11.837C67.3137 41.9471 66.5845 28.7779 65.7202 0h-1.4404c-.9003 28.8049-1.5845 41.9471-11.8387 52.4429C41.9439 62.6956 28.7819 63.4157 0 64.2799v1.4402c28.8089.9002 41.9439 1.5843 52.4411 11.837C62.6953 88.0529 63.4155 101.222 64.2798 130h1.4404c.9003-28.805 1.5935-41.9471 11.8387-52.4429C88.0561 67.3044 101.218 66.5843 130 65.7201z" fill="white"></path></svg>
            </p>
            </div>
          </v-col>
          <v-col
          v-else
          class="result"
          >
            <div >
              <h1>
                ТВОЯ ЦЕЛЬ:
              </h1>
              <p>
                {{query}}
              </p>
              <p class="smart-p"
              v-bind:class="{ active: sActive }">
                <span>
                  S
                </span>
              </p>
              <p class="smart-p"
              v-bind:class="{ active: mActive }">
                <span>
                  M
                </span>
              </p class="smart-p">
              <p class="smart-p"
              v-bind:class="{ active: aActive }">
                <span>
                  A
                </span>
              </p >
              <p class="smart-p"
              v-bind:class="{ active: rActive }">
                <span>
                  R
                </span>
              </p>
              <p class="smart-p"
              v-bind:class="{ active: tActive }">
                <span>
                  T
                </span>
              </p>

              </p>
            </div>
            <div>
              <p>
                <img v-if="eduActive" v-bind:class="{ active: eduActive }" class="attr-image" src="../assets/img/mortarboard-gray.svg" alt="avatar" />
                <img v-else class="attr-image" src="../assets/img/mortarboard-gray-unactive.svg" alt="avatar" />
                <img v-if="unamActive" v-bind:class="{ active: unamActive }" class="attr-image" src="../assets/img/precision-gray.svg" alt="avatar" />
                <img v-else  class="attr-image" src="../assets/img/precision-gray-unactive.svg" alt="avatar" />
              </p>
            </div>
            <div>
              <p id="p-button">
                <v-btn
                class="ma-2"
                color="secondary"
                @click="resetResult = 'resetResulloading'"
                >
                СБРОСИТЬ РЕЗУЛЬТАТ
              </v-btn>
            </p>
            </div>
          </v-col>
        </v-row>
      </v-container>
      <div class=" text-center">
      <v-dialog
        v-model="dialog"
        width="500"
      >

        <v-card>
          <v-card-title class="modal-grad headline orange ">
            <p>
              Попробуй сформулировать свою цель <br /> иначе
            </p>
          </v-card-title>

          <v-card-text class="black-text">
            <h>НАПРИМЕР:</h>
            <p>
              Увеличить продажи бренда А на территории России к концу года на 25%
            </p>
            <p>
              Достичь уровня знания товара А среди молодой аудитории на уровне 51% через 3 года, после запуска товара на рынок.
            </p>
            <p>
              Завести бренд компании в количестве 3 SKU в ТОП-10 ключевых торговых сетей до июля 2014 года.
            </p>
          </v-card-text>

          <v-divider></v-divider>

          <v-card-actions class="modal-grad">
            <v-spacer></v-spacer>
            <v-btn
              color="black"
              text
              @click="dialog = false"
            >
              Ввести заново
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </div>
        <v-footer
    padless
  >
    <v-card
      flat
      tile
      class="orange lighten-2 lighten-1 white--text text-center"
    >
      <v-card-text>
        <v-btn
          v-for="icon in icons"
          :key="icon"
          class="mx-4 white--text"
          icon
        >
          <v-icon size="24px">
            {{ icon }}
          </v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0">
        SMART / SMARTER — это мнемоническая аббревиатура, используемая в менеджменте и проектном управлении для определения целей и постановки задач. Схема постановки целей SMART создана Джорджем Дораном (англ. George T. Doran) в 1981 году.
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>KOVALEV.TEAM</strong>
      </v-card-text>
    </v-card>
  </v-footer>
  </v-main>
</template>

<script>
import MainCardComponent from "@/components/node/MainCardComponent";
import NodesService from "@/services/NodesService.js";

  const gradients = [
    ['#222'],
    ['#42b3f4'],
    ['red', 'orange', 'yellow'],
    ['purple', 'violet'],
    ['#00c6ff', '#F0F', '#FF0'],
    ['#f72047', '#ffd200', '#1feaea'],
  ]

export default {
	name: "Main",
  components: {
		MainCardComponent
	},
	async mounted() {

    setTimeout(() => {  this.kLogoDelay = true }, 700);
    setTimeout(() => {  this.logoDelay = true }, 1800);
    setTimeout(() => {  this.titleDelay = true }, 2200);
	},
	data: () => ({
    nodes: [],
    width: 2,
    radius: 10,
    padding: 8,
    lineCap: 'round',
    gradient: gradients[5],
    value: [0, 2, 5, 9, 5, 10, 3, 5, 0, 0, 1, 8, 2, 9, 0],
    gradientDirection: 'top',
    gradients,
    fill: false,
    type: 'trend',
    autoLineWidth: false,
    kLogoDelay: false,
    titleDelay: false,
    logoDelay: false,
    icons: [
      'mdi-facebook',
      'mdi-twitter',
      'mdi-linkedin',
      'mdi-instagram',
    ],
    loader: null,
    resetResult: null,
    resetResulloading: false,
    loading: false,
    result: {},
    query: "",
    service: NodesService,
    dialog: false,
	}),
	computed: {
    firstStyle() {
      return {
        "background-color": "black",
      };
    },
    showResult() {
      return Object.keys(this.result).length == 0
    },
    sActive(){
      return !!this.result['S']
    },
    mActive(){
      return !!this.result['M']
    },
    aActive(){
      return !!this.result['A']
    },
    rActive(){
      return !!this.result['R']
    },
    tActive(){
      return !!this.result['T']
    },
    eduActive(){
      return !!this.result['education']
    },
    unamActive(){
      return !!this.result['unambiguity']
    },
    additionals(){
      var arr = []

      if (!!this.result["education"]){
        arr.push({
          name: "Ваша цель относится к образованию",
          desc: "Да"
        })
      }

      if (!!this.result["unambiguity"]){
        arr.push({
          name: "Ваша цель однозначна",
          desc: "Да"
        })
      }
      return arr;
    }
	},
   watch: {
      async loader () {
        const l = this.loader
        this[l] = !this[l]
        this.loader = null
        this[l] = false
        if (this.query?.split(" ").length < 3 ||
        ['кто','что', '?', 'кого', "чего", "кому", "чему", "кого", "кем", "зачем", "почему"].includes(this.query?.split(" ")[0].toLowerCase()) ||
        this.query?.split(" ").includes("?")
        ){
          this.dialog = true;
        }else{
          this.result = await this.service.query(this.query)
        }
      },
      resetResult () {
        const r = this.resetResult
        this[r] = !this[r]
        this.resetResult = null
        this.result = {}
        this.query = ""
      }
    },
    metaInfo() {
          return {
              title: "SMART",
              meta: [
                  { name: 'description', content:  ''},
                  { property: 'og:title', content: "SMART"},
                  { property: 'og:site_name', content: 'SMART.KOVALEV.TEAM'},
                  {property: 'og:type', content: 'website'},
                  {property: 'og:image', content: '../assets/img/logo.png'},
              ]
          }
    }

};
</script>

<style scoped lang="scss">
  #main-container{
    max-width: 100%;
    max-height: 100%;
    min-height: 100%;
    padding: 0;
  }
  .main-card{
    width: 100%;
    height: 100%;
    margin: 0;
    border-radius: 6% 6% 0% 0% / 7% 7% 0% 0%;
    padding-bottom: 100px;
    margin-bottom: -100px;
    div{
      position: relative;
      width: 80%;
      min-height: 93vh;
      margin-left: auto;
      margin-right: auto;
    }
  }

  #main-logo{
    width: 140px;
    height: 70px;
    margin-left: 10%;
  }

  #main-container{
    background-color: black;
  }

  #first-main{
    background-color: black;
    color: white;
    border-radius: 0% 0% 0% 0% / 0% 0% 0% 0%;
    figure{
      margin-left: auto;
      margin-right: auto;
      max-width: 80%;
    }
  }
  #second-main{
    background-color: white;
    div{
      margin-top: 30px;
    }
    p{
      font-size: 30px;
    }
  }
  #third-main{
    background: rgb(253,29,29);
    background: linear-gradient(153deg, rgba(253,29,29,1) 0%, rgba(252,176,69,1) 11%);
    p{
      width: 15%;
      float: left;
      margin-left: 50px;
      text-align: justify;
      span{
        text-align: center;
        font-size: 120px;
      }
      img{
        width: 100%;
        opacity: 0.9;
        border-radius: 30% 70% 70% 30% / 30% 30% 70% 70% ;
        margin-top: 20px;
      }
    }
    div{
      min-height: 1vh !important;
    }
  }
  #four-main{
    background-color: black;
    color: white;
    h2{
      text-align: center;
    }
    div.v-textarea{
      margin-top: 20px;
      min-height: 0;
    }
    p{
      text-align: center;
    }
    svg.little{
      width: 200px;
      height: 200px;
    }
    svg.big{
      width: 400px;
      height: 400px;
      position: relative;
      margin-left: 70%;
    }
    .result{
      img{
        opacity: 0.1;
      }
      img.active{
        opacity: 1 !important;
      }
      div{
        width: 80%;
        min-height: 200px;
        margin-left: auto;
        margin-right: auto;
      }
      p.active{
        background: linear-gradient(153deg, rgba(253,29,29,1) 0%, rgba(252,176,69,1) 11%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        opacity: 1 !important;
      }
      p.smart-p{
        opacity: 0.1;
        width: 15%;
        float: left;
        margin-left: 50px;
        text-align: justify;
        span{
          text-align: center;
          font-size: 120px;
        }
      }
      #p-button{
        text-align: center;
      }
      h1{
        text-align: center;
      }
      .v-data-table{
        border-radius: 7px;
      }
    }
  }
  .attr-image{
    width: 150px;
    margin-right: 50px;
  }
  .modal-grad{
    background: rgb(253,29,29) !important;
    background: linear-gradient(153deg, rgba(253,29,29,1) 0%, rgba(252,176,69,1) 11%) !important;
  }
  .black-text{
    color: black !important;
  }

  footer{
    div{
      width: 100%;
    }
  }
</style>
