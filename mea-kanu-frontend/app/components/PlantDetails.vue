<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <NavigationButton @tap="$navigateBack()" android.systemIcon="ic_menu_back" />
            <Label class="action-bar-title" :text="plantData.commonName" horizontalAlignment="center" />
        </ActionBar>

        <ScrollView>
            <StackLayout>
                <Image :src="plantData.picture" stretch="aspectFill" height="300" class="" />

                <Label row="1" class="hr-light m-b-15"/>

                <GridLayout row="2" rows="*, *, *, *, *, *, *" columns="auto, auto">

                    <Label text="Scientific Name" row="0" class="p-l-15 p-b-10 m-r-20 text-primary big" />
                    <Label :text="plantData.species" row="0" col="1" class="text p-b-10 big"/>

                    <Label text="Hawaiian Name" row="1" class="p-l-15 p-b-10 m-r-20 text-primary big" />
                    <Label :text="plantData.hawaiianName" row="1" col="1" class="text p-b-10 big" />

                    <Label text="Conservation Status" row="2" class="p-l-15 p-b-10 m-r-20 text-primary big" />
                    <Label :text="plantData.conservationStatus" row="2" col="1" class="text p-b-10 big" />

                    <Label text="Status" row="3" class="p-l-15 p-b-10 m-r-20 text-primary big" />
                    <Label :text="plantData.status" row="3" col="1" class="text p-b-10 big" />
                </GridLayout>

                <Label row="2" class="hr-light m-t-15 m-b-15"/>

                    <StackLayout>
                        <Label text="Uses" row="1" class="p-l-15 p-b-10 m-r-10 h1" />
                        <Label :text="plantData.uses" class="text p-l-15 p-r-15 p-b-10 big" textWrap="true"></Label>

                        <Label class="hr-light m-t-15 m-b-15"/>

                        <Label text="Mo'olelo (Story)" class="p-l-15 p-b-10 m-r-10 h1" />
                        <Label :text="plantData.story" class="text p-l-15 p-r-15 p-b-10 big" textWrap="true"></Label>

                        <Label class="hr-light m-t-15 m-b-15"/>

                        <Label text="Description" row="1" class="p-l-15 p-b-10 m-r-10 h1" />
                        <Label :text="plantData.description" class="text p-l-15 p-r-15 p-b-10 big" textWrap="true"></Label>

                        <Label class="hr-light m-t-15 m-b-15"/>

                    </StackLayout>


                    <!--<Label text="Moolelo" row="5" class="p-l-15 p-b-10 m-r-10 text-primary big" />-->
                    <!--<Label textWrap="true" :text="plantData.story" row="5" col="1" class="body p-b-10 big" ></Label>-->

                    <!--<Label text="Description" row="6" class="p-l-15 p-b-10 m-r-10 text-primary big" />-->
                    <!--<Label textWrap="true" :text="plantData.description" row="6" col="1"  class="text p-b-10 big"></Label>-->




                <!--<Button class="btn btn-primary" text="button"/>-->
            </StackLayout>
        </ScrollView>
    </Page>
</template>

<script>
    import CarDetailsEdit from "./CarDetailsEdit";

    export default {
        props: ["plant"],

        computed: {
            plantData() {
                return this.plant || {};
            }
        },

        methods: {
            onEditButtonTap() {
                this.$navigateTo(CarDetailsEdit, {
                    transition: "slideTop",
                    backstackVisible: false,
                    props: { car: this.carData }
                });
            }
        }
    };
</script>
<style>
    .big {
        font-size: 15;
    }
</style>