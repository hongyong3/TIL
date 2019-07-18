<template>
  <div>
    <Navbar />
    <br />
    <FineDust></FineDust>
  </div>
</template>

<script>
import FineDust from "@/components/finedust/FineDust";
import Navbar from "@/components/mainview/Navbar";

export default {
  name: "FineDust2",
  components: {
    FineDust,
    Navbar,
  }
};
</script>
