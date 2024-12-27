declare module "*.vue" {
    import { DefineComponent } from "vue";
    const App: DefineComponent<{}, {}, any>;
    export default App;
}