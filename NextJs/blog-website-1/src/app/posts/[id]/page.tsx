import NotFound from "./not-found";

type PostPageProps = {
  params: {
    id: string;
  };
};

export default async function PostPage({ params }: PostPageProps) {
  const response = await fetch(`https://dummyjson.com/posts/${params.id}`);
  const post = await response.json();

  if (!post.title) {
    return <NotFound />;
  }

  return (
    <main className="main-page text-center pt-32 px-5">
      <h1>{post.title}</h1>
      <p className="max-w-[700px] mx-auto">{post.body}</p>
    </main>
  );
}
