<template>
  <div>
    <Navbar />
    <Loader />
    <main class="py-3">
      <router-view />
    </main>
    <Footer />
  </div>
</template>

<script>
import Navbar from "@/components/Navbar.vue"
import Footer from "@/components/Footer.vue"
import Loader from "@/components/Loader.vue"
import axios from "axios"
export default {
  name: "App",
  beforeCreate() {
    this.$store.commit("initializeStore")

    const token = this.$store.state.token

    if (token) {
      axios.defaults.headers.common["Authorization"] = "Token " + token
    } else {
      axios.defaults.headers.common["Authorization"] = ""
    }
  },
  components: {
    Navbar,
    Footer,
    Loader,
  },
}
</script>

<style lang="scss">
.btn {
  border-radius: 0;
  // height: 55px;
  padding: 10px;
  text-transform: uppercase;
}
.btn-dark[disabaled] {
  background: #55595c;
}

.uppercase {
  text-transform: uppercase;
}

.form-control {
  outline: none !important;
  border: 0 !important;
  color: rgb(110, 110, 110) !important;
  height: 45px;
}

.form-control:focus {
  border-radius: 0;
}

input[type="radio"] {
  background-color: initial;
  cursor: default;
  appearance: auto;
  box-sizing: border-box;
  margin: 3px 3px 0px 5px;
  padding: initial;
  border: initial;
}

.list-group-item {
  position: relative;
  display: block;
  font-weight: lighter;
  font-size: 18px;
  padding: 0.75rem 1.25rem;
  color: #212529;
  text-decoration: none;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, 0.125);
}

a {
  text-decoration: none;
  color: black;
}

.underline:hover {
  text-decoration: underline;
  color: black;
}

h1,
h2,
h3,
h4,
h5,
h6 {
  font-weight: 400;
  letter-spacing: 2px;
}

strong {
  font-weight: bolder;
}

.col {
  color: #55595c;
}

.is-loading-bar {
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading {
    height: 80px;
  }
}

.lds-default {
  display: inline-block;
  position: relative;
  width: 80px;
  height: 80px;
}
.lds-default div {
  position: absolute;
  width: 6px;
  height: 6px;
  background: rgb(47, 50, 83);
  border-radius: 50%;
  animation: lds-default 1.2s linear infinite;
}
.lds-default div:nth-child(1) {
  animation-delay: 0s;
  top: 37px;
  left: 66px;
}
.lds-default div:nth-child(2) {
  animation-delay: -0.1s;
  top: 22px;
  left: 62px;
}
.lds-default div:nth-child(3) {
  animation-delay: -0.2s;
  top: 11px;
  left: 52px;
}
.lds-default div:nth-child(4) {
  animation-delay: -0.3s;
  top: 7px;
  left: 37px;
}
.lds-default div:nth-child(5) {
  animation-delay: -0.4s;
  top: 11px;
  left: 22px;
}
.lds-default div:nth-child(6) {
  animation-delay: -0.5s;
  top: 22px;
  left: 11px;
}
.lds-default div:nth-child(7) {
  animation-delay: -0.6s;
  top: 37px;
  left: 7px;
}
.lds-default div:nth-child(8) {
  animation-delay: -0.7s;
  top: 52px;
  left: 11px;
}
.lds-default div:nth-child(9) {
  animation-delay: -0.8s;
  top: 62px;
  left: 22px;
}
.lds-default div:nth-child(10) {
  animation-delay: -0.9s;
  top: 66px;
  left: 37px;
}
.lds-default div:nth-child(11) {
  animation-delay: -1s;
  top: 62px;
  left: 52px;
}
.lds-default div:nth-child(12) {
  animation-delay: -1.1s;
  top: 52px;
  left: 62px;
}
@keyframes lds-default {
  0%,
  20%,
  80%,
  100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.5);
  }
}
.spinner-border {
  display: inline-block;
  width: 2rem;
  height: 2rem;
  vertical-align: text-bottom;
  border: 0.25em solid;
  border-right: 0.25em solid transparent;
  border-radius: 50%;
  -webkit-animation: spinner-border 0.75s linear infinite;
  animation: spinner-border 0.75s linear infinite;
}

.page-link {
  border: 0;
}
.page-item .page-link {
  color: #55595c;
}
.page-item.active .page-link {
  background: #1a1a1a;
  border-radius: 0;
}
.card-img {
  object-fit: cover;
}
</style>
