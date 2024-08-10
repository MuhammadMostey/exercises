import PostsLists from "../../components/PostsLists/PostsLists";

export default async function PostsPage() {
  const numberOfPosts = 10;
  const response = await fetch(
    `https://dummyjson.com/posts?limit=${numberOfPosts}`,
    {
      next: {
        revalidate: 3600,
      },
    }
  );

  const data = await response.json();

  return (
    <main className="text-center pt-24 px-5 main-page">
      <h1>All Posts</h1>
      <PostsLists posts={data.posts} />
    </main>
  );
}
