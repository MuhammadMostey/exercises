import "../../app/globals.css";
import Link from "next/link";

type PostsListProps = {
  posts: Post[];
};

export default function PostsList({ posts }: PostsListProps) {
  return (
    <>
      <ul>
        {posts.map((post) => (
          <li
            key={post.id}
            className="max-w-[400px] mb-3 mx-auto hover:text-blue-300 "
          >
            <Link href={`/posts/${post.id}`}>{post.title}</Link>
          </li>
        ))}
      </ul>
    </>
  );
}
