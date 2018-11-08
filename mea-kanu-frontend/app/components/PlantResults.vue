<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <NavigationButton @tap="$navigateBack()" android.systemIcon="ic_menu_back" />
            <Label class="action-bar-title" text="Results" horizontalAlignment="center" />
        </ActionBar>

        <RadListView ref="listView" for="(plant,index) in plantData"  @itemTap="onItemTap" class="list-group">
            <ListViewLinearLayout v-tkListViewLayout scrollDirection="vertical"/>
            <v-template>

                <GridLayout rows="*, *, *" columns="*, *" class="list-group-item-content">
                    <Label :text="plant.commonName"
                           class="text-primary list-group-item-text font-weight-bold"/>

                    <Label row="1" class="hr-dark m-t-5 m-b-5" colSpan="2"/>

                    <Image row="2" :src="plant.picture" stretch="aspectFill" height="120" class="m-r-20" loadMode="async"/>

                    <StackLayout row="2" col="1" verticalAlignment="center" class="list-group-item-text">
                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf12a;   " class="fa text-primary"/>
                                <Span :text="plant.conservationStatus"/>
                            </FormattedString>
                        </Label>

                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf0c3;   " class="fa text-primary"/>
                                <Span :text="plant.species"/>
                            </FormattedString>
                        </Label>

                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf0ac;   " class="fa text-primary"/>
                                <Span :text="plant.hawaiianName"/>
                            </FormattedString>
                        </Label>
                        <Label :text="percentData[index]+'% Accuracy'" col="1" horizontalAlignment="left" class="p-b-10 font-weight-bold"/>
                    </StackLayout>
                </GridLayout>

            </v-template>

        </RadListView>
    </Page>
</template>

<script>
    import PlantDetails from "./PlantDetails";

    export default {
        props: ["plantResults", "percentages"],

        // computed: {
        //     resultData() {
        //         return this.plantResults || [];
        //     }
        // },
        data() {
            return {
                plantData: this.plantResults,
                percentData: this.percentages
            }
        },
        methods: {
            onItemTap(e) {
                this.$emit("select", e.item);
                //console.log(e);
                // console.log(e.item);
                //console.log(e.item.name);
                // console.log(e.plant);
                this.$navigateTo(PlantDetails, {props: {plant: e.item}});
            }
        },
        created() {
            console.log("In PlantAResults.vue");
            console.log(this.plantData);
            console.log(this.plantData[0]);
            console.log(this.plantData[0].species);
            console.log(this.percentData[0]);

        }
    }
</script>
<style scoped lang="scss">
    @import '../app-variables';
    // End custom common variables

    // Custom styles
    .list-picture {
        height: 100;
        width: 100;
    }

    .list-group {
        .list-group-item-content {
            padding: 8 15 4 15;
            background-color: $background-light;
        }

        .list-group-item-text {
            margin: 2 3;
        }

        .fa {
            color: $accent-dark;
        }
    }

    .back {
        background-color: gray;
    }
</style>