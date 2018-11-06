<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <NavigationButton @tap="$navigateBack()" android.systemIcon="ic_menu_back" />
            <Label class="action-bar-title" :text="plantData.name" horizontalAlignment="center" />
        </ActionBar>

        <ScrollView>
            <StackLayout>
                <Image :src="plantData.picture" stretch="aspectFill" height="300" class="m-b-15" />

                <Label row="1" class="hr-light m-t-15 m-b-15"/>

                <GridLayout row="2" rows="*, *, *, *, *, *" columns="auto,auto">

                    <Label text="Scientific Name" row="0" class="p-l-15 p-b-10 m-r-20 text-primary big" />
                    <Label :text="plantData.scientificName" row="0" col="1" class="text p-b-10 big"/>

                    <Label text="Hawaiian Name" row="1" class="p-l-15 p-b-10 m-r-20 text-primary big" />
                    <Label :text="plantData.hawaiianName" row="1" col="1" class="text p-b-10 big" />

                    <Label text="Status" row="2" class="p-l-15 p-b-10 m-r-20 text-primary big" />
                    <Label :text="plantData.label" row="2" col="1" class="text p-b-10 big" />

                </GridLayout>
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