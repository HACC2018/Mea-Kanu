<template>
    <Page class="page">
        <ActionBar class="action-bar">
            <Label class="action-bar-title" text="Mea Kanu" horizontalAlignment="center"/>
            <ActionItem @tap="uploadPicture" android.systemIcon="ic_menu_upload" android.position="actionBar"/>
            <NavigationButton text="Go Back" android.systemIcon="ic_menu_camera" @tap="openCam"/>
        </ActionBar>
        <RadListView ref="listView" for="plant in plantList" @itemTap="onItemTap" class="list-group">
            <ListViewLinearLayout v-tkListViewLayout scrollDirection="vertical"/>
            <v-template>

                <GridLayout rows="*, *, *" columns="*, *" class="list-group-item-content">
                    <Label :text="plant.name" class="text-primary list-group-item-text font-weight-bold"/>
                    <Label col="1" horizontalAlignment="right" class="list-group-item-text m-r-5"/>

                    <Label row="1" class="hr-dark m-t-5 m-b-5" colSpan="2"/>

                    <Image row="2" :src="plant.picture" stretch="aspectFill" height="120" class="m-r-20"
                           loadMode="async"/>
                    <StackLayout row="2" col="1" verticalAlignment="center" class="list-group-item-text">
                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf12a;   " class="fa text-primary"/>
                                <Span :text="plant.label"/>
                            </FormattedString>
                        </Label>

                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf0ac;   " class="fa text-primary"/>
                                <Span :text="plant.scientificName"/>
                            </FormattedString>
                        </Label>

                        <Label class="p-b-10">
                            <FormattedString>
                                <Span text.decode="&#xf0c3;   " class="fa text-primary"/>
                                <Span :text="plant.hawaiianName"/>
                            </FormattedString>
                        </Label>
                    </StackLayout>
                </GridLayout>

                <!--<StackLayout orientation="vertical">-->
                <!--<Label :text="plant.name"></Label>-->
                <!--<Image :src="plant.picture" class="list-picture"/>--
            <!--</StackLayout>-->
            </v-template>

        </RadListView>
    </Page>
</template>

<script>

    import * as camera from "nativescript-camera";
    import axios from 'axios';
    //import * as axios from "axios/dist/axios";
    import * as imageSource from "tns-core-modules/image-source";
    import PlantDetails from "./PlantDetails";

    var imagepicker = require("nativescript-imagepicker");
    const enums = require("ui/enums");
    export default {

        data() {
            return {
                picture: null,
                imagePicker: [],
                pictureBase64String: '',
                pictureAxios: null,
                plantList: [
                    {
                        class: 0,
                        name: "Abutilon menziesii",
                        scientificName: "Abutilon menziesii",
                        hawaiianName: "Koʻoloaʻula",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Abutilon menziesii, known as Ko'oloa'ula in Hawaiian, is an endangered species of flowering shrub in the mallow family, Malvaceae, that is endemic to Hawaii. It inhabits dry forests on the islands of Lanai, Maui, Oahu and Hawaii."
                    },
                    {
                        class: 1,
                        name: "Maui chaff flower",
                        scientificName: "Achyranthes splendens",
                        hawaiianName: "Ewa hinahina",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Achyranthes splendens is a species of flowering plant in the pigweed family, Amaranthaceae, that is endemic to Hawai?i. Its natural habitats are dry forests, low shrublands, and sandy shores. It is threatened by habitat loss."
                    },
                    {
                        class: 2,
                        name: "Hawaiʻi Lady's Nightcap",
                        scientificName: "Bonamia menziesii",
                        hawaiianName: "Hawaiian bonamia",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Bonamia menziesii, commonly known as Hawai?i lady's nightcap, is a species of flowering plant in the morning glory family, Convolvulaceae, that is endemic to Hawaii. It is a vine or twisting liana with branches that can reach 10 m in length."
                    },
                    {
                        class: 3,
                        name: "Sticky Flatsedge",
                        scientificName: "Cyperus trachysanthos",
                        hawaiianName: "pu`uka`a",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Cyperus trachysanthos is a rare species of sedge known by the common names pu`uka`a and sticky flatsedge. It is endemic to Hawaii, where it is known from Kauai and Oahu. It was known from Niihau, Molokai and Lanai, but it has been extirpated from these islands."
                    },
                    {
                        class: 4,
                        name: "hairyfruit chewstick",
                        scientificName: "Gouania hillebrandii",
                        hawaiianName: "Oʻahu chewstick",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Gouania hillebrandii is an endangered species of Gouania that is endemic to Hawaii. It formerly could be found on Maui, Moloka?i, L?na?i and Kaho?olawe, but is today restricted to western Maui near Lahaina. It inhabits dry forests at elevations of 244–518 m."
                    },
                    {
                        class: 5,
                        name: "Hawaiian Hibiscus",
                        scientificName: "Hibiscus brackenridgei",
                        hawaiianName: "Maʻo hau hele",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Hawaiian hibiscus are seven species of hibiscus regarded as native to Hawaii. The yellow hibiscus is Hawaii's state flower."
                    },
                    {
                        class: 6,
                        name: "Carter's panicgrass",
                        scientificName: "Panicum fauriei",
                        hawaiianName: "none",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Panicum fauriei is a species of grass known by the common name Faurie's panicgrass. It is endemic to Hawaii. There are at least three varieties of this grass species. One, var. carteri, Carter's panicgrass is federally listed as an endangered species of the United States."
                    },
                    {
                        class: 7,
                        name: "Portulaca villosa",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Portulaca oleracea is an annual succulent in the family Portulacaceae, which may reach 40 cm in height. Approximately forty cultivars are currently grown."
                    },
                    {
                        class: 8,
                        name: "Scaevola coriacea",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Scaevola coriacea, the dwarf naupaka, is a species of flowering plant in the Goodenia family, Goodeniaceae, that is endemic to Hawaii."
                    },
                    {
                        class: 9,
                        name: "Sesbania tomentosa",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Sesbania tomentosa, commonly known as Oahu riverhemp and ??hai, is an endangered species of flowering plant in the pea family, Fabaceae, that is endemic to the main Hawaiian Islands as well as Nihoa and Necker Island."
                    },
                    {
                        class: 10,
                        name: "Acacia confusa",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Some common names for it are acacia petit feuille, small Philippine acacia, Formosa acacia (Taiwan acacia) and Formosan koa. It grows to a height of 50 ft. The tree has become very common in many tropical Pacific areas, including Hawaii, where the species is considered invasive."
                    },
                    {
                        class: 11,
                        name: "Acalypha hispida",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly called chenille plant and red-hot cat's tail is a beautiful flowering plant that has a long bloom period. This plant is also known as the Philippines Medusa, pokok ekor kucing in Malay, Rabo de Gato in Portuguese, and shibjhul in Bengali. Acalypha hispida is cultivated as a house plant because of its attractiveness and brilliantly colored, furry flowers."
                    },
                    {
                        class: 12,
                        name: "Aloe vera",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names include Chinese Aloe, Indian Aloe, True Aloe, Barbados Aloe, Burn Aloe, First Aid Plant. An evergreen perennial, it originates from the Arabian Peninsula but grows wild in tropical climates around the world and is cultivated for agricultural and medicinal uses. The species is also used for decorative purposes and grows successfully indoors as a potted plant."
                    },
                    {
                        class: 13,
                        name: "Alpinia purpurata",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The red ginger, also called ostrich plume and pink cone ginger, is a species with showy flowers on long brightly colored red bracts. It prefers partial shade and moist humid conditions, although it can tolerate full sun in some climates. It tends to like to be well watered and not left to dry out. Ginger can also be grown as a houseplant and its cut flowers can be used in arrangements."
                    },
                    {
                        class: 14,
                        name: "Anthurium andreanum",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names for this species include tailflower, flamingo flower, and laceleaf. Its name comes from the Greek words anthos, meaning flower, and oura, meaning a tail. It is a monocotyledonous perennial, preferring warm, shady and humid climates, such as tropical rainforests. Its most characteristic feature as an ornamental is its brightly colored spathe leaf, and the protruding inflorescence called the spadix."
                    },
                    {
                        class: 15,
                        name: "Bauhinia variegata",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names include orchid tree, camel's foot tree, kachnar, and mountain-ebony. This is a very popular ornamental tree in subtropical and tropical climates. It is a small to medium-sized tree growing up to 39 ft tall, deciduous in the dry season. This is a very popular ornamental tree in subtropical and tropical climates, grown for its scented flowers and also used as food item in South Asian cuisine."
                    },
                    {
                        class: 16,
                        name: "Bixa orellana",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as Achiote, this species is a shrub or small tree originating from the tropical region of the Americas. North, Central, and South American natives originally used the seeds to make red body paint and lipstick, as well as a spice. For this reason, the achiote is sometimes called the lipstick tree."
                    },
                    {
                        class: 17,
                        name: "Blighia sapida",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The ackee, also known as achee, ackee apple or ayee is a fruit, which is the member of the Sapindaceae (soapberry family). Ackee is an evergreen tree that grows about 33 ft tall, with a short trunk and a dense crown. Although native to West Africa, the use of ackee in food is especially prominent in Jamaican cuisine. Ackee is the national fruit of Jamaica, and ackee and saltfish is the national dish."
                    },
                    {
                        class: 18,
                        name: "Bombax glabra",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as Malabar Chestnut, Pachira aquatica, Guiana chestnut, provision tree, saba nut, Monguba, Pumpo and is commercially sold under the names money tree and money plant. This tree is sometimes sold with a braided trunk and is commonly grown as a houseplant."
                    },
                    {
                        class: 19,
                        name: "Bougainvillea sp",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as great bougainvillea, is a species of flowering plant. This plant is also widely grown as an ornamental plant. It grows as a woody vine or shrub, reaching up to 40 feet with heart-shaped leaves and thorny, pubescent stems. The flowers are generally small, white, and inconspicuous, highlighted by several brightly colored modified leaves called bracts."
                    },
                    {
                        class: 20,
                        name: "Brugmansia x candida",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Their large, fragrant flowers give them their common name of angel's trumpets. They are woody trees or shrubs, with pendulous flowers, and have no spines on their fruit. They are large shrubs or small trees, with semi-woody, often many-branched trunks. They can reach heights up to 36 ft. The leaves are alternately arranged along the stems with an entire or coarsely toothed margin, and are often covered with fine hairs. "
                    },
                    {
                        class: 21,
                        name: "Caesalpinia pulcherrima",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names for this species include poinciana, peacock flower, red bird of paradise, dwarf poinciana, flos pavonis, flamboyant-de-jardin and ohai ali'i in Hawaiian. It is a shrub growing to 10 ft tall. In climates with few to no frosts, this plant will grow larger and is semievergreen. Grown in climates with light to moderate freezing, plant will die back to the ground depending on cold, but will rebound in mid- to late spring."
                    },
                    {
                        class: 22,
                        name: "Calotropis gigantea",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly called crown flower or giant milkweed, is a large shrub or small tree cultivated in tropical areas around the world. It is a large shrub growing to 13 ft tall. It has clusters of waxy flowers that are either white or lavender in colour. Each flower consists of five pointed petals and a small \"crown\" rising from the center which holds the stamens. "
                    },
                    {
                        class: 23,
                        name: "Canna indica",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as Indian shot, African arrowroot, edible canna, purple arrowroot, Sierra Leone arrowroot, is a plant species in the family Cannaceae. It has been cultivated by indigenous peoples of the Americas in tropical America for thousands of years. The place of the first domestication may have been the northern Andes, as may be true of other similar root crops."
                    },
                    {
                        class: 24,
                        name: "Cardiospermum grandiflorum",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as balloon vine, heart pea or heart seed, is a species of climbing plant. It can grow over 33 ft long and it has small white flowers. It is also a weed of forests and forest margins, urban bushland, open woodlands, roadsides, fence-lines, disturbed sites, waste areas and neglected gardens in tropical, sub-tropical and warmer temperate regions."
                    },
                    {
                        class: 25,
                        name: "Cascabela thevetia",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as yellow oleander or lucky nut, these flowers are used for religious purpose especially in the worshipping of the God Shiva. It is an evergreen tropical shrub or small tree. Its leaves are willow-like, linear-lanceolate, and glossy green in color. They are covered in waxy coating to reduce water loss (typical of oleanders). Its stem is green turning silver/gray as it ages."
                    },
                    {
                        class: 26,
                        name: "Cassia bakeriana",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly called pink shower or wishing tree, is a small flowering tree that typically matures up to 3 ft tall and as wide. This tree is now grown primarily as an ornamental in tropical and subtropical areas around the world. It is noted for producing a showy display of fragrant pink-purple flowers with yellow stamens."
                    },
                    {
                        class: 27,
                        name: "Casuarina equisetifolia",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names include coast sheoak, beach casuarina, beach oak, whistling tree, horsetail she oak, horsetail beefwood, horsetail tree and agoho. Casuarina equisetifolia is an evergreen tree growing up to 115 ft tall. The foliage consists of slender bearing minute scale-leaves in whorls of 6–8. The flowers are produced in small catkin-like inflorescences."
                    },
                    {
                        class: 28,
                        name: "Catharanthus roseus",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as the Madagascar periwinkle, rose periwinkle, or rosy periwinkle, is a species of flowering plant in the dogbane family Apocynaceae. In the wild, it is an endangered plant; the main cause of decline is habitat destruction by slash and burn agriculture. It is also however widely cultivated and is naturalised in subtropical and tropical areas of the world."
                    },
                    {
                        class: 29,
                        name: "Cattleya sp",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names are Cattleya Orchid and Corsage Orchid, like most orchids, priced for it's delicate and beautiful flowers. Epiphytic or terrestrial orchids with cylindrical rhizome from which the fleshy noodle-like roots grow. Pseudobulbs can be conical, spindle-shaped or cylindrical; with upright growth; one or two leaves growing from the top of them."
                    },
                    {
                        class: 30,
                        name: "Chlorophytum comosum",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Often called spider plant but also known as airplane plant, St. Bernard's lily, spider ivy, ribbon plant, and hen and chickens is a species of perennial flowering plant. Chlorophytum comosum is a popular houseplant. The species with all-green leaves forms only a small proportion of plants sold. More common are two variegated cultivars: 'Vittatum' with a broad central white stripe and 'Variegatum' with white margins."
                    },
                    {
                        class: 31,
                        name: "Clerodendrum quadriloculare",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also called bronze-leaved clerodendrum, fire works, Philippine glorybower, shooting star or starburst bush, these plants produce flowers that can be a pest to eradicate. This is one of the tropic's most beautiful flowering shrubs. Large, dark-green and burgundy leaves are the backdrop for firework-resembling, pink and white flower clusters in late winter and early spring."
                    },
                    {
                        class: 32,
                        name: "Clitoria ternatea",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as Asian pigeonwings, bluebellvine, blue pea, butterfly pea, cordofan pea and Darwin pea, is a plant species belonging to the Fabaceae family. The flowers of this vine were imagined to have the shape of human female genitals, hence the Latin name of the genus \"Clitoria\", from \"clitoris\"."
                    },
                    {
                        class: 33,
                        name: "Cocos nucifera",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The coconut palm, is a monocot perennial member of the Arecaceae family, cultivated in tropical areas worldwide for its fruit and fiber. Coconut palms are medium-sized, solitary herbaceous plants. Although treelike in form, their trunks are composed not of wood, but of fibrous, stout, overlapping stems, and may grow to 80 ft tall."
                    },
                    {
                        class: 34,
                        name: "Codiaeum variegatum",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Garden croton or variegated croton, this is a species of plant in the genus Codiaeum, which is a member of the family Euphorbiaceae. There are several hundred cultivars, selected and bred for their foliage. Depending on the cultivar, the leaves may be ovate to linear, entire to deeply lobed or crinkled, and variegated with green, white, purple, orange, yellow, red or pink."
                    },
                    {
                        class: 35,
                        name: "Couroupita guianensis",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Known by a variety of names including cannonball tree, it is cultivated in many tropical areas because of its beautiful, fragrant flowers and large fruits. Couroupita guianensis is a tree that reaches heights of up to 110 ft tall. It is planted as an ornamental for its showy, scented flowers, and as a botanical specimen for its interesting fruit."
                    },
                    {
                        class: 36,
                        name: "Crescentia cujete",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as the Calabash Tree, is species of flowering plant with simple leaves, which are alternate or in fascicles on short shoots. The fruit, called Jícara, Bule, Tecomate, Guaje, Morro or Huacal in Mexico, is used to make small vessels for serving or drinking. ,The tree shares its common name with that of the vine calabash, or bottle gourd."
                    },
                    {
                        class: 37,
                        name: "Crinum asiaticum",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as poison bulb, giant crinum lily, grand crinum lily, or spider lily, this is a plant species widely planted in many warmer regions as an ornamental. It is a bulb-forming perennial producing an umbel of large, showy flowers that are prized by gardeners. All parts of the plant are, however, poisonous if ingested. Some reports indicate exposure to the sap may cause skin irritation."
                    },
                    {
                        class: 38,
                        name: "Cupressus sempervirens",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as Italian cypress, Tuscan cypress, Persian cypress, or pencil pine, this is a medium-sized coniferous evergreen tree to 115 ft tall. It is a medium-sized coniferous evergreen tree to 115 ft tall, with a conic crown with level branches and variably loosely hanging branchlets. It is very long-lived, with some trees reported to be over 1,000 years old."
                    },
                    {
                        class: 39,
                        name: "Cyperus papyrus",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Known as papyrus, papyrus sedge, paper reed, Indian matting plant, and Nile grass, this is a species of aquatic flowering plant belonging to the family Cyperaceae. It has a very long history of use by humans, it is the source of papyrus paper. Parts of the plant can be eaten, and the highly buoyant stems can be made into boats. It is now often cultivated as an ornamental plant."
                    },
                    {
                        class: 40,
                        name: "Delonix regia",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The flame tree is a species of flowering plant in the bean family Fabaceae. It is noted for its fern-like leaves and flamboyant display of flowers. In many tropical parts of the world it is grown as an ornamental tree and in English it is given the name royal poinciana or flamboyant. It is also one of several trees known as \"flame tree\"."
                    },
                    {
                        class: 41,
                        name: "Dendrobium sp",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "These plants belong to a large and diverse genus of orchids. The name is from the Greek dendron (\"tree\") and bios (\"life\"); it means \"one who lives on trees\". They are either epiphytic, or occasionally lithophytic. They have adapted to a wide variety of habitats, from the high altitudes in the Himalayan mountains to lowland tropical forests and even to the dry climate of the Australian desert."
                    },
                    {
                        class: 42,
                        name: "Dichorisandra thyrsiflora",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The blue ginger is a species of tropical flowering plant which resembles ginger in growth and habit but is actually related to the spiderworts (the genus Tradescantia). it is cultivated for its handsome spotted stems and large shiny foliage which is held horizontally, surmounted by striking blue flowers. The Latin specific epithet thyrsiflora means “with flower clusters resembling thyme”."
                    },
                    {
                        class: 43,
                        name: "Eichhornia crassipes",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as common water hyacinth, is an aquatic plant and often a highly problematic invasive species. One of the fastest growing plants known, water hyacinth reproduces primarily by way of runners or stolons, which eventually form daughter plants. Each plant additionally can produce thousands of seeds each year, and these seeds can remain viable for more than 28 years."
                    },
                    {
                        class: 44,
                        name: "Erythrina crista-galli",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Often known as the cockspur coral tree, is a flowering tree in the family Fabaceae. It is known by several common names such as ceibo, seíbo, corticeira, and bucaré. This species characteristically grows wild in gallery forest ecosystems along watercourses, as well as in swamps and wetlands. In urban settings, it is often planted in parks for its bright red flowers."
                    },
                    {
                        class: 45,
                        name: "Eucalyptus deglupta",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as the rainbow eucalyptus, Mindanao gum, or rainbow gum. It is characterized by multi-colored bark featuring hues of blue, purple, orange and maroon. It thrives in rich, medium to wet soil in full sun and is intolerant of frost. In its native habitat, it grows up to 6 ft wide and over  250 ft tall."
                    },
                    {
                        class: 46,
                        name: "Eugenia uniflora",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as pitanga, Suriname cherry, Brazilian cherry, Cayenne cherry, or Cerisier Carré, is a plant in the family Myrtaceae. It is characterized by multi-colored bark featuring hues of blue, purple, orange and maroon. It thrives in rich, medium to wet soil in full sun and is intolerant of frost."
                    },
                    {
                        class: 47,
                        name: "Ficus microcarpa",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as Chinese banyan, Malayan banyan, Indian laurel, curtain fig, or gajumaru, is a tree in the fig family Moraceae. The largest known specimen is at the Menehune Botanical Gardens near Nawiliwili, Kauai, Hawai'i which is 110 ft in height, 250 ft in crown spread, and having over one thousand aerial trunks."
                    },
                    {
                        class: 48,
                        name: "Filicium decipiens",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Known as fern tree, Japanese fern tree, Pihimbiya, or Thika palm, is a slow-growing tree with a straight, short trunk and a dense, neatly shaped rounded crown. It is a pleasant and graceful specimen whose small size makes it ideal for your yard or home landscape. The tree is most easily recognizable for its odd foliage."
                    },
                    {
                        class: 49,
                        name: "Gardenia brighamii",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as nanu, na'u, or forest gardenia, is a species of flowering plant in the coffee family, Rubiaceae, that is endemic to Hawaii. It is a small tree, reaching a height of 16 ft. The glossy, dark green leaves are ovate. The petals of the solitary, white flowers are fused at the base and have six lobes."
                    },
                    {
                        class: 50,
                        name: "Gomphrena globosa",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as globe amaranth, makhmali, and vadamalli, is an edible plant from the family Amaranthaceae. The round-shaped flower inflorescences are a visually dominant feature and cultivars have been propagated to exhibit shades of magenta, purple, red, orange, white, pink, and lilac. Within the flowerheads, the true flowers are small and inconspicuous."
                    },
                    {
                        class: 51,
                        name: "Guaiacum officinale",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as roughbark lignum-vitae, guaiacwood or gaďacwood, is a species of tree in the caltrop family named Zygophyllaceae. This small tree is very slow growing, reaching about 33 ft in height. The tree is essentially evergreen throughout most of its native range. The blue flowers have five petals that yield a bright-yellow-orange fruit with red flesh and black seeds."
                    },
                    {
                        class: 52,
                        name: "Harpullia pendula",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Known as the tulipwood or tulip lancewood, is a small to medium-sized rainforest tree. The tree's size, pleasant form and attractive fruit ensures its popularity of this ornamental tree. Tulipwood occurs in various types of rainforest, by streams or dry rainforests on basaltic or alluvial soils. In tropical and sub tropical rainforest. "
                    },
                    {
                        class: 53,
                        name: "Hedychium coronarium",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as white garland-lily or white ginger lily, is a perennial flowering plant in the Zingiberaceae (ginger) family. It is commonly cultivated in warm temperate and subtropical regions of the world as an ornamental and cultivated in China for use in medicine and production of aromatic oil due to its strong characteristic fragrance of the flowers said to be reminiscent of jasmine."
                    },
                    {
                        class: 54,
                        name: "Hemigraphis alternata",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as red ivy, red-flame ivy, or waffle plant, is a member of the Acanthaceae family. It is a prostrate plant with purple colored leaves. The leaves are hairy and opposite, and one leaf of a pair is much larger than the other.  The flowers of the plant grow from where the leaf meets the stem, and are white with purple penciling."
                    },
                    {
                        class: 55,
                        name: "Hibiscus rosa-sinensis",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Known colloquially as Chinese hibiscus, China rose, Hawaiian hibiscus, rose mallow or shoeblackplant, is a flowering plant in the Hibisceae tribe of the family Malvaceae. It is a bushy, evergreen shrub or small tree growing up to 16 ft tall, with glossy leaves and solitary, brilliant red flowers in summer and autumn with prominent orange-tipped red anthers."
                    },
                    {
                        class: 56,
                        name: "Hippeastrum reticulatum",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly know as netted-veined amaryllis, is a flowering perennial herbaceous bulbous plant, in the Amaryllidaceae family. A defining characteristic of this species is an unusual and exquisite venation of the petals, darker than the purple to pink background color. The seeds are unusual for Hippeastrum in being orange-red, round, turgid and fleshy rather than black and paper like."
                    },
                    {
                        class: 57,
                        name: "Impatiens wallerana",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as busy Lizzie, balsam, sultana, or simply impatiens, is a flowering herbaceous perennial plant growing up to 2 ft tall. Leaves are mostly alternate, although they may be opposite near the top of the plant. The stems are semi-succulent, and all parts of the plant (leaves, stems, flowers, roots) are soft and easily damaged."
                    },
                    {
                        class: 58,
                        name: "Ixora sp",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names include viruchi, rangan, kheme, ponna, chann tanea, techi, pan, siantan, jarum-jarum/jejarum, jungle flame, jungle geranium, cruz de Malta among others. Though native to the tropical and subtropical areas throughout the world, its centre of diversity is in Tropical Asia. It also grows commonly in subtropical climates in the United States, such as Florida where it is commonly known as West Indian Jasmine."
                    },
                    {
                        class: 59,
                        name: "Jasminum sambac",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The Arabian jasmine, is a species of jasmine cultivated in many places for its attractive and sweetly fragrant flowers. It is a small shrub or vine growing up to 10 ft in height. The flowers may be used as a fragrant ingredient in perfumes and jasmine tea. It is the national flower of the Philippines, where it is known as sampaguita, as well as being one of the three national flowers of Indonesia, where it is known as melati putih."
                    },
                    {
                        class: 60,
                        name: "Justicia brandegeana",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Mexican shrimp plant, shrimp plant or false hop, is an evergreen shrub in the genus Justicia of the family Acanthaceae. The flowers are white, extending from red bracts which look a bit like a shrimp, hence the shrub's common name, shrimp flower.The species is named after the American botanist Townshend Stith Brandegee."
                    },
                    {
                        class: 61,
                        name: "Kigelia africana",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Kigelia is a genus of flowering plants in the family Bignoniaceae. Other common names are sausage tree, cucumber tree, and sausage-like fruit. It is a bushy evergreen shrub growing to 3 ft tall. The stems and leaves are downy. The leaves are variegated and usually grow in clusters on the branches. As the plant receives more sun, the amount of creamy white on the speckled leaves will increase, and vice versa."
                    },
                    {
                        class: 62,
                        name: "Koelreuteria formosana",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "More commonly known as Flamegold rain tree or Taiwanese rain tree, is a deciduous tree up to 50 ft tall. It is widely grown throughout the tropics and sub-tropical parts of the world as a street tree. It flowers in early to mid-summer. Flowers are small and occur in branched clusters at the stem tips. They are butter-yellow with five petals that vary in length until opening."
                    },
                    {
                        class: 63,
                        name: "Lantana montevidensis",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Known by many common names, such as trailing lantana, weeping lantana, creeping lantana, small lantana, purple lantana or trailing shrubverbena. It is a small strongly scented flowering low shrub with oval-shaped green leaves. With support it has a climbing 'vine' form, when on edge a trailing form, and on the flat a groundcover form."
                    },
                    {
                        class: 64,
                        name: "Leea guineensis",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly called, West Indian holly, Hawaiian holly or burgundy leea, is a tropical evergreen shrub to small tree that typically grows in outdoor. This is an understory species that typically grows in its native habitat on forest floors in shady locations under the cover of taller trees where it typically adapts well to low light levels."
                    },
                    {
                        class: 65,
                        name: "Litchi chinensis",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Llitchi, liechee, liche, lizhi or li zhi, or lichee, is the sole member of the genus Litchi in the soapberry family, Sapindaceae. A tall evergreen tree, the lychee bears small fleshy fruits. The outside of the fruit is pink-red, roughly textured and inedible, covering sweet flesh eaten in many different dessert dishes. Since the perfume-like flavor is lost in the process of canning, the fruit is usually eaten fresh."
                    },
                    {
                        class: 66,
                        name: "Lonicera japonica",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Known as golden-and-silver honeysuckle and Japanese honeysuckle, is a twining vine able to climb up to 33 ft high or more in trees. The flowers are double-tongued, opening white and fading to yellow, and sweetly vanilla scented. The fruit is a black spherical berry containing a few seeds. This species is often sold by American nurseries as the cultivar 'Hall's Prolific'."
                    },
                    {
                        class: 67,
                        name: "Lophostemon confertus",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names include brush box, Queensland box, Brisbane box, pink box, box scrub, and vinegartree. In the wild its habitat ranges from moist open forest and rainforest ecotones, where it might reach heights of 130 ft or more, to coastal headlands where it acquires a stunted, wind-sheared habit. Dome-like in shape, it has a denser foliage with dark green, leathery leaves and hence provides more shade than eucalypts."
                    },
                    {
                        class: 68,
                        name: "Magnolia grandiflora",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as the southern magnolia or bull bay, is a tree of the family Magnoliaceae. Reaching 90 ft in height, it is a large striking evergreen tree. Although endemic to the lowland subtropical forests on the Gulf and south Atlantic coastal plain, it is widely cultivated in warmer areas around the world. The timber is hard and heavy, and has been used commercially to make furniture, pallets, and veneer."
                    },
                    {
                        class: 69,
                        name: "Mangifera indica",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as mango, is a species of flowering plant in the sumac and poison ivy family Anacardiaceae. Hundreds of cultivated varieties have been introduced to other warm regions of the world. It is a large fruit-tree, capable of a growing to a height and crown width of about 100 ft and trunk circumference of more than 12 ft."
                    },
                    {
                        class: 70,
                        name: "Metrosideros polymorpha",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The Ohi'a lehua, is a species of flowering evergreen tree in the myrtle family, Myrtaceae, that is endemic to the six largest islands of Hawaii. It is a highly variable tree, being up to 82 ft tall in favorable situations, and a much smaller prostrate shrub when growing in boggy soils or directly on basalt. It produces a brilliant display of flowers, made up of a mass of stamens, which can range from fiery red to yellow."
                    },
                    {
                        class: 71,
                        name: "Musa x paradisiaca",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "This is the accepted name for the hybrid between Musa acuminata and Musa balbisiana. Almost all cultivated plantains and many cultivated bananas are triploid cultivars of this species. It is believed that Southeast Asian farmers first domesticated M. acuminata. When the cultivated plants spread north-west into areas where M. balbisiana was native."
                    },
                    {
                        class: 72,
                        name: "Nandina domestica",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as nandina, heavenly bamboo or sacred bamboo, is a species of flowering plant in the family Berberidaceae. Despite the common name, it is not a bamboo but an erect evergreen shrub up to 7 ft tall, with numerous, usually unbranched stems growing from ground level. The glossy leaves are sometimes deciduous in colder areas."
                    },
                    {
                        class: 73,
                        name: "Norantea guianensis",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as Red Hot Poker Vine, Red Popcorn, Conoro-antegri, or Karakara, is a large woody vine, climbing up to 30 ft with adventitious roots. Leaves glossy green, smooth and thick; young leaves orangey or reddish.Flowers small and insignificant, borne along middle axis of elongated terminal racemes."
                    },
                    {
                        class: 74,
                        name: "Orthosiphon aristatus",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "It is known as kumis kucing in Indonesia and misai kucing in Malaysia. In the US it may be commonly known as cat's whiskers or Java tea. It is mainly taken to stimulate urination. According to Indonesian and Malaysian folk medicine, bladder or kidney pain, gout, rheumatism and arteriosclerosis can be treated by drinking a decoction of leaves boiled in water."
                    },
                    {
                        class: 75,
                        name: "Pandanus tectorius",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names include Tahitian screwpine, thatch screwpine, hala tree, pandanus, and pu hala in Hawaiian. The fruit is sometimes known as hala fruit. is a small tree that grows upright to reach up to 46 ft in height. It is supported by prop roots that firmly anchors the tree to the ground. Roots sometimes grow along the branch, and they grow a wide angles in proportion to the trunk."
                    },
                    {
                        class: 76,
                        name: "Pentas lanceolata",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as Egyptian starcluster, is known for its wide use as a garden plant where it often accompanies butterfly gardens. It is a tropical woody-based perennial or subshrub that grows 6 ft tall in its native habitat. It is also a many-branched, somewhat sprawling plant that features rounded clusters of star-shaped flowers over a long summer to frost bloom. "
                    },
                    {
                        class: 77,
                        name: "Petrea volubilis",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Petrea is a genus of evergreen flowering vines that have rough-textured leaves, hence the common name sandpaper vine. The tubular blue flowers only last a few days but the larger and more showy bluish purple calyces remain, fading first to blue and finally to a pale gray color. The dark green foliage acts as a foil to the pale calyces, so that the floral display appears as pale stars on a dark background."
                    },
                    {
                        class: 78,
                        name: "Phytolacca dioica",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as ombú, is a massive evergreen tree and has an umbrella-like canopy that spreads to a diameter up to 50 ft and can attain a height up to 60 ft. Because it is derived from herbaceous ancestors, its trunk consists of anomalous secondary thickening rather than true wood. As a result, the ombú grows fast but its wood is soft and spongy enough to be cut with a knife."
                    },
                    {
                        class: 79,
                        name: "Plectranthus scutellarioides",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly known as coleus, is a species of flowering plant in the family Lamiaceae. Another common name is painted nettle, reflecting its relationship to deadnettles. Typically growing to 2 ft tall and wide, it is a bushy, woody-based evergreen perennial, widely grown for the highly decorative variegated leaves found in cultivated varieties."
                    },
                    {
                        class: 80,
                        name: "Podranea ricasoliana",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Podranea, is a genus of one or two species of African flowering vines in the Bignoniaceae family. It is a very showy plant with its glossy foliage and abundance of attractive pink flowers. It is also a vigorous, woody, rambling, evergreen climber without tendrils. The leaves are compound and a deep glossy green."
                    },
                    {
                        class: 81,
                        name: "Portulacaria afra",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as elephant bush, dwarf jade plant, porkbush, and spekboom, is a small-leaved succulent plant. It is a soft-wooded, semi-evergreen upright shrub or small tree, usually up to 15 ft tall. It is popular as an indoor bonsai, and as a hardy xeriscaping plant. Several varieties exist - some bred in cultivation, others naturally occurring."
                    },
                    {
                        class: 82,
                        name: "Punica granatum",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The pomegranate is a fruit-bearing deciduous shrub or small tree in the family Lythraceae that grows up to 33 ft tall. As intact arils or juice, pomegranates are used in baking, cooking, juice blends, meal garnishes, smoothies, and alcoholic beverages, such as cocktails and wine. The French term for pomegranate, grenade, has given its name to the military grenade."
                    },
                    {
                        class: 83,
                        name: "Pyrostegia venusta",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also commonly known as flamevine or orange trumpetvine, is a plant species of the genus Pyrostegia of the family Bignoniaceae, nowadays a well-known garden species. It is one of the most spectacular flowering vines in cultivation. It is a vigorous, evergreen liana (a name for large woody climbers) that can spread quickly by tendrils to the top of whatever supports it."
                    },
                    {
                        class: 84,
                        name: "Quisqualis indica",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as the Chinese honeysuckle or Rangoon creeper, is a vine with red flower clusters. The Rangoon creeper is a ligneous vine that can reach up to 26 ft. The leaves are elliptical with an acuminate tip and a rounded base, and the flowers are fragrant and tubular and their color varies from white to pink to red. "
                    },
                    {
                        class: 85,
                        name: "Rhaphiolepis umbellata",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "This is a species of flowering plant in the Rosaceae family. Growing to 5 ft tall and wide, it is an evergreen shrub with glossy oval leaves, and scented white flowers, sometimes tinged with pink, in early summer. This plant has gained the Royal Horticultural Society's Award of Garden Merit. It is used in Japan as an astringent and a dyeing agent."
                    },
                    {
                        class: 86,
                        name: "Solanum seaforthianum",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The Brazilian nightshade, is a flowering evergreen vine of the Solanaceae family. It is characterized by clusters of four to seven leaves and can climb to a height of 20 ft given enough room. It blooms in the mid to late summer with clusters of star-shaped purple inflorescence followed by scarlet marble-sized berries. The plant is highly heat resistant, but cannot tolerate frost conditions."
                    },
                    {
                        class: 87,
                        name: "Stemmadenia littoralis",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The milky way tree is an open-branching tree that creates a multi-layered canopy. In the tropics, these trees have a maximum height of around 25 ft. The tubular white flowers of Stemmadenia littoralis can be found on the tree from spring through fall. Only when the cool winter nights set in does the tree stop flowering. While in flower, it is a remarkably floriferous tree."
                    },
                    {
                        class: 88,
                        name: "Strelitzia reginae",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Common names include strelitzia, crane flower or bird of paradise, though these names are also collectively applied to other species in the genus Strelitzia. The plant grows to 6.6 ft tall, with large, strong leaves. They are evergreen leaves and arranged in two ranks, making a fan-shaped crown. The flowers stand above the foliage at the tips of long stalks. "
                    },
                    {
                        class: 89,
                        name: "Symphytum officinale",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Other names include Quaker comfrey, cultivated comfrey, boneset, knitbone, consound, and slippery-root. The hardy plant can grow to a height of 4 ft. Its roots have been used in the traditional Balkan medicine internally (as tea or tincture) or externally (as ointment, compresses,or alcoholic digestion) for treatment of disorders of the locomotor system and gastrointestinal tract."
                    },
                    {
                        class: 90,
                        name: "Tabebuia impetiginosa",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Known as pink ipę, pink lapacho, or pink trumpet tree is a native tree of family Bignoniaceae. It is a conspicuous and well-known species with a long history of human use. Consequently, it has a range of local names: ipę-cavată, ipę-comum, ipę-reto, ipę-rosa, ipę-roxo-damata, lapacho negro, pau d'arco-roxo, peúva or piúva."
                    },
                    {
                        class: 91,
                        name: "Tabernaemontana divaricata",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Apocynaceae, commonly called pinwheelflower, crape jasmine, East India rosebay and Nero's crown is an evergreen shrub. The plant generally grows to a height of 5–6 ft and is dichotomously-branched. The large shiny leaves are deep green. The waxy blossoms are found in small clusters on the stem tips. The plant blooms in spring but flowers appear sporadically all year. "
                    },
                    {
                        class: 92,
                        name: "Tamarindus indica",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Tamarind is a leguminous tree in the family Fabaceae. The genus Tamarindus is a monotypic taxon, having only a single species. The tamarind tree produces pod-like fruit, which contain an edible pulp that is used in cuisines around the world. Other uses of the pulp include traditional medicine and metal polish. The wood can be used for woodworking, and tamarind seed oil can be extracted from the seeds."
                    },
                    {
                        class: 93,
                        name: "Terminalia catappa",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "It is known by the English common names country-almond, Indian-almond, Malabar-almond, sea-almond, tropical-almond and false kamani. The tree grows up to 115 ft tall, with an upright, symmetrical crown and horizontal branches. Terminalia catappa has corky, light fruit that are dispersed by water. The seed within the fruit is edible when fully ripe, tasting almost like almond."
                    },
                    {
                        class: 94,
                        name: "Thunbergia battescombei",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Known as the scrambling sky flower, is a herbaceous weak stemmed perennial vine that tends to lean upon other plants for support. So scrambling clock vine is a herbaceous weak stemmed perennial vine that tends to lean upon other plants for support. When unsupported it will form a symmetrical mound of flopped over stems that is about 4 ft high by 6 ft wide. "
                    },
                    {
                        class: 95,
                        name: "Tipuana tipu",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Also known as tipa, rosewood, and pride of Bolivia, is the only member of the genus Tipuana and well-known for its use as a shade tree. It is viewed as an invasive weed in some countries and is known for having a very aggressive root system. The tree roots can easily lift up concrete and asphalt. Precautions should be taken when planting near buildings, homes, or pools, as they are likely to be damaged."
                    },
                    {
                        class: 96,
                        name: "Tradescantia spathacea",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The boatlily or Moses-in-the-cradle, has fleshy rhizomes and rosettes of waxy lance-shaped leaves. Leaves are dark to metallic green above, with glossy purple underneath. It has fleshy rhizomes and rosettes of waxy lance-shaped leaves. Leaves are dark to metallic green above, with glossy purple underneath. They are very attractive foliage plants that will reach 1 ft tall."
                    },
                    {
                        class: 97,
                        name: "Turnera ulmifolia",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The ramgoat dashalong or yellow alder, is a species of plant of family Passifloraceae. It grows erect, with dark toothed leaves and small, yellow-orange flowers, and is often found as a weed growing on roadsides. This plant is commonly misidentified with the closely related T. diffusa in horticultural commerce, causing it to be often misrepresented as \"Damiana.\""
                    },
                    {
                        class: 98,
                        name: "Vitex rotundifolia",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "The roundleaf chastetree or beach vitex is a species of Vitex, this woody perennial plant typically grows approximately 3 ft in height. Its range includes continents and islands stretching from India east to Hawaii and from Korea south to Australia. It has a sprawling growth habit and produces runners that root regularly at nodes."
                    },
                    {
                        class: 99,
                        name: "Youngia japonica",
                        scientificName: "",
                        hawaiianName: "",
                        picture: "",
                        native: true,
                        endangered: true,
                        description: "Commonly called Oriental false hawksbeard, is a species of flowering plant in the aster family. Native to eastern Asia, it is now found as a weed nearly worldwide. It is an annual that produces yellow flowers. In tropical areas, it can bloom year round, while in temperate areas it blooms in late spring and early summer. Stems are usually solitary and erect. Basal leaves are large a pinnately divided. Its fruits are wind dispersed."
                    },
                    {
                        name: "Acalypha Hispida",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'invasive',
                        picture: "~/images/Acalypha_hispida.jpg"
                    },
                    {
                        name: "Alocasia Macrorrhiza",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'endangered',
                        picture: "~/images/Alocasia_macrorrhiza.jpg"
                    },
                    {
                        name: "Aloe Vera",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'invasive',
                        picture: "~/images/Aloe_vera.jpg"
                    },
                    {
                        name: "Alpinia Purpurata",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'endangered',
                        picture: "~/images/Alpinia_purpurata.jpg"
                    },
                    {
                        name: "Anthurium Andreanum",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'endangered',
                        picture: "~/images/Anthurium_andreanum.jpg"
                    },
                    {
                        name: "Azadirachta Indica",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'invasive',
                        picture: "~/images/Azadirachta_indica.jpg"
                    },
                    {
                        name: "Bauhinia Variegata",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'endangered',
                        picture: "~/images/Bauhinia_variegata.jpg"
                    },
                    {
                        name: "Bixa Orellana",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'invasive',
                        picture: "~/images/Bixa_orellana.jpg"
                    },
                    {
                        name: "Blighia Sapida",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'endangered',
                        picture: "~/images/Blighia_sapida.jpg"
                    },
                    {
                        name: "Bombax Glabra",
                        scientificName: 'placeholder',
                        hawaiianName: 'hawaii placeholder',
                        label: 'invasive',
                        picture: "~/images/Bombax_glabra.jpg"
                    },
                ]
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
            },
            openCam() {
                camera.requestPermissions();
                // console.log("1");
                camera
                    .takePicture({width: 300, height: 300, keepAspectRatio: true, saveToGallery: true})
                    .then(imageAsset => {
                        // console.log("2");
                        console.log(imageAsset);
                        this.picture = imageAsset;
                        // console.log("5");
                        let source = new imageSource.ImageSource();
                        // console.log("6");
                        source.fromAsset(imageAsset).then(source => {
                            // console.log("4");
                            this.pictureBase64String = source.toBase64String("png", 100);
                            console.log(this.pictureBase64String);
                            // console.log("Here I am");
                        });
                        // console.log("Is axios doing anything?");
                        axios.post('https://mea-kanu.firebaseio.com/data.json', {ImageContent: this.pictureBase64String.toString()})
                            .then(response => {
                                let result = response.data;
                                // console.log("Success: firebase is responding to your shit");
                                // console.log(result);
                            }, error => {
                                console.error(error);
                            });

                    })
            },
            uploadPicture() {
                console.log("Hitting uploadPicture");
                console.log(this.pictureBase64String);
                let context = imagepicker.create({mode: "single"});
                context
                    .authorize()
                    .then(function () {
                        console.log("fuck1");
                        return context.present();
                    })
                    .then(function (selection) {
                        console.log("fuck2");
                        selection.forEach(function (selected) {
                        });

                        console.log("fuck3");
                        //console.log(selected);
                        let source = new imageSource.ImageSource();
                        console.log("fuck4");
                        // console.log(context);
                        // console.log(selection);
                        // console.log(selection[0]);
                        source.fromAsset(selection[0]).then(source => {
                            console.log("hello");

                            //  console.log(source.toBase64String("png", 100));
                            //  console.log("what is going on");
                            console.log(this.pictureBase64String);
                            this.pictureBase64String = source.toBase64String("png", 100);
                            console.log(this.pictureBase64String);
                            console.log("Here I am");
                        });
                        axios.post('https://mea-kanu.firebaseio.com/data.json', {ImageContent: source.toBase64String("png", 100).toString()})
                            .then(response => {
                                let result = response.data;
                                console.log("Success: firebase is responding to your shit");
                                console.log(result);
                            }, error => {
                                console.log("HEREIAM");
                                console.error(error);
                            });

                    }).catch(function (e) {
                    console.error(e);
                });
                // axios.post('https://mea-kanu.firebaseio.com/data.json', {ImageContent: this.pictureBase64String.toString()})
                //     .then(response => {
                //         let result = response.data;
                //         console.log("Success: firebase is responding to your shit");
                //         console.log(result);
                //     }, error => {
                //         console.log("HEREIAM");
                //         console.error(error);
                //     });
            },
            goBack() {
                console.log('testing goBack function is this getting updated');
            },
            sendPicture() {
                console.log('this should appear');
            }

        },
        // created() {
        //
        // let imageModule = require('ui/image');
        // camera.takePicture({width:300, height:300, saveToGallery: true})
        //     .then(function (imageAsset){
        //         console.log("Result is an image asset instance");
        //         let image = new imageModule.Image();
        //         image.src = imageAsset;
        //     }).catch(function (err) {
        //         console.log("Error -> " + err.message);
        // });
        // }
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

<!--<RadListView v-if="!isLoading" for="item in carList" @itemTap="onItemTap" class="list-group">-->
<!--<ListViewLinearLayout v-tkListViewLayout scrollDirection="Vertical"/>-->
<!--<v-template>-->
<!--<GridLayout rows="*, *, *" columns="*, *" class="list-group-item-content">-->
<!--<Label :text="item.name" class="text-primary list-group-item-text font-weight-bold"/>-->
<!--<Label col="1" horizontalAlignment="right" class="list-group-item-text m-r-5">-->
<!--<FormattedString>-->
<!--<Span text.decode="&euro;"/>-->
<!--<Span :text="item.price"/>-->
<!--<Span text="/day"/>-->
<!--</FormattedString>-->
<!--</Label>-->

<!--<Label row="1" class="hr-light m-t-5 m-b-5" colSpan="2"/>-->

<!--<Image row="2" :src="item.imageUrl" stretch="aspectFill" height="120" class="m-r-20" loadMode="async"/>-->

<!--<StackLayout row="2" col="1" verticalAlignment="center" class="list-group-item-text">-->
<!--<Label class="p-b-10">-->
<!--<FormattedString ios.fontFamily="system">-->
<!--<Span text.decode="&#xf1b9;   " class="fa text-primary"></Span>-->
<!--<Span :text="item.class"/>-->
<!--</FormattedString>-->
<!--</Label>-->
<!--<Label class="p-b-10">-->
<!--<FormattedString ios.fontFamily="system">-->
<!--<Span text.decode="&#xf085;   " class="fa text-primary"/>-->
<!--<Span :text="item.transmission"/>-->
<!--<Span text=" Transmission"/>-->
<!--</FormattedString>-->
<!--</Label>-->
<!--<Label class="p-b-10">-->
<!--<FormattedString ios.fontFamily="system">-->
<!--<Span text.decode="&#xf2dc;   " class="fa text-primary"/>-->
<!--<Span :text="item.hasAC ? 'Yes' : 'No'"/>-->
<!--</FormattedString>-->
<!--</Label>-->
<!--</StackLayout>-->
<!--</GridLayout>-->
<!--</v-template>-->
<!--</RadListView>-->
<!--<ActivityIndicator v-else :busy="isLoading"/>-->
<!--</Page>-->
<!--</template>-->

<!--<script>-->
<!--import CarDetails from "./CarDetails";-->

<!--export default {-->
<!--computed: {-->
<!--carList() {-->
<!--return this.$root.cars;-->
<!--},-->

<!--isLoading() {-->
<!--return !this.carList.length;-->
<!--}-->
<!--},-->

<!--methods: {-->
<!--onItemTap(e) {-->
<!--this.$emit("select", e.item);-->
<!--this.$navigateTo(CarDetails, { props: { car: e.item } });-->
<!--}-->
<!--}-->
<!--};-->
<!--</script>-->

<!--<style scoped lang="scss">-->
<!--// Start custom common variables-->
<!--@import '../app-variables';-->
<!--// End custom common variables-->

<!--// Custom styles-->
<!--.list-group {-->
<!--.list-group-item-content {-->
<!--padding: 8 15 4 15;-->
<!--background-color: $background-light;-->
<!--}-->

<!--.list-group-item-text {-->
<!--margin: 2 3;-->
<!--}-->

<!--.fa {-->
<!--color: $accent-dark;-->
<!--}-->
<!--}-->
<!--</style>-->
