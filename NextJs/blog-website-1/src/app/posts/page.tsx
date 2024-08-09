import PostsLists from "../../components/PostsLists/PostsLists";

export default function Home() {
  return (
    <main className="text-center pt-32 px-5 main-page">
      <h1>All Posts</h1>
      <PostsLists />
    </main>
  );
}
